package main

import (
	"bytes"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"os"
	"regexp"
	"strings"
)

func main() {
	// Create a cookie jar to maintain session cookies
	jar, err := cookiejar.New(nil)
	if err != nil {
		log.Fatalf("Failed to create cookie jar: %v", err)
	}

	client := &http.Client{
		Jar: jar,
		CheckRedirect: func(req *http.Request, via []*http.Request) error {
			// Copy cookies and other headers from the original request
			for _, v := range via {
				for key, vals := range v.Header {
					for _, val := range vals {
						req.Header.Add(key, val)
					}
				}
			}
			return nil
		},
	}

	initialURL := "https://piee.eb.mil/sol/xhtml/unauth/search/oppMgmtLink.xhtml?solNo=W911S225U0427"
	htmlContent, err := fetchHTML(client, initialURL)
	if err != nil {
		log.Fatalf("Failed to fetch initial HTML: %v", err)
	}

	log.Println("Successfully fetched the initial page")

	// Try multiple ViewState extraction patterns
	viewState, err := extractViewState(htmlContent)
	if err != nil {
		log.Fatalf("Failed to extract ViewState: %v", err)
	}
	log.Printf("Found ViewState: %s", viewState)

	// Extract form action URL
	actionURL, err := extractFormAction(htmlContent, initialURL)
	if err != nil {
		log.Fatalf("Failed to extract form action URL: %v", err)
	}
	log.Printf("Form action URL: %s", actionURL)
	
	// Extract other form parameters that might be needed
	formId := extractFormId(htmlContent)
	log.Printf("Form ID: %s", formId)
	
	// Extract downloadAllAttachments button ID
	downloadButtonId := extractDownloadButtonId(htmlContent)
	log.Printf("Download button ID: %s", downloadButtonId)

	// Prepare form data for the download request
	formData := url.Values{}
	formData.Set("form", formId)
	formData.Set("form_SUBMIT", "1")
	formData.Set("javax.faces.ViewState", viewState)
	
	// Add the specific button that was clicked
	// This is important for JSF forms to know which button triggered the action
	formData.Set(downloadButtonId, downloadButtonId)

	// You may need additional parameters based on the JSF implementation
	formData.Set("javax.faces.source", downloadButtonId)
	formData.Set("javax.faces.partial.event", "click")
	formData.Set("javax.faces.partial.execute", downloadButtonId + " " + formId)
	formData.Set("javax.faces.partial.render", formId)
	formData.Set("javax.faces.behavior.event", "action")

	// Make the POST request to download
	log.Println("Sending download request...")
	req, err := http.NewRequest("POST", actionURL, bytes.NewBufferString(formData.Encode()))
	if err != nil {
		log.Fatalf("Failed to create request: %v", err)
	}

	// Set headers similar to a browser
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
	req.Header.Set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
	req.Header.Set("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
	req.Header.Set("Accept-Language", "en-US,en;q=0.5")
	req.Header.Set("Connection", "keep-alive")
	req.Header.Set("Upgrade-Insecure-Requests", "1")
	req.Header.Set("Cache-Control", "max-age=0")

	resp, err := client.Do(req)
	if err != nil {
		log.Fatalf("Failed to make POST request: %v", err)
	}
	defer resp.Body.Close()

	log.Printf("Response status: %s", resp.Status)

	// Debug headers
	log.Println("Response headers:")
	for name, values := range resp.Header {
		for _, value := range values {
			log.Printf("%s: %s", name, value)
		}
	}

	// Get Content-Type to determine if we got the file or an HTML page
	contentType := resp.Header.Get("Content-Type")
	
	if strings.Contains(contentType, "text/html") {
		// If we got HTML back, it might be an error page or redirect
		responseBody, err := io.ReadAll(resp.Body)
		if err != nil {
			log.Fatalf("Failed to read response body: %v", err)
		}
		
		// Save the response to analyze what went wrong
		err = os.WriteFile("response.html", responseBody, 0644)
		if err != nil {
			log.Fatalf("Failed to save response: %v", err)
		}
		log.Println("Got HTML response instead of file. Saved as response.html for debugging.")
		
		// Try to find any error messages
		errorRegex := regexp.MustCompile(`<div[^>]*class="[^"]*error[^"]*"[^>]*>(.*?)</div>`)
		errorMatches := errorRegex.FindAllStringSubmatch(string(responseBody), -1)
		if len(errorMatches) > 0 {
			for _, match := range errorMatches {
				log.Printf("Possible error message: %s", match[1])
			}
		}
		
		return
	}

	// Get filename from Content-Disposition header
	contentDisposition := resp.Header.Get("Content-Disposition")
	filename := extractFilenameFromContentDisposition(contentDisposition)
	if filename == "" {
		log.Println("No filename found in Content-Disposition, using default")
		filename = "downloaded_file.zip"
	}

	file, err := os.Create(filename)
	if err != nil {
		log.Fatalf("Failed to create file: %v", err)
	}
	defer file.Close()

	_, err = io.Copy(file, resp.Body)
	if err != nil {
		log.Fatalf("Failed to save file: %v", err)
	}

	fmt.Printf("File downloaded successfully: %s\n", filename)
}

func fetchHTML(client *http.Client, url string) (string, error) {
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return "", err
	}

	// Add browser-like headers
	req.Header.Set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
	req.Header.Set("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
	req.Header.Set("Accept-Language", "en-US,en;q=0.5")

	resp, err := client.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	bodyBytes, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}
	return string(bodyBytes), nil
}

func extractViewState(html string) (string, error) {
	// Try different patterns for ViewState
	patterns := []string{
		`name="javax.faces.ViewState"[^>]+value="([^"]+)"`,
		`id="[^"]*javax.faces.ViewState[^"]*"[^>]+value="([^"]+)"`,
		`<input[^>]+name="javax.faces.ViewState"[^>]+value="([^"]+)"`,
		`<input[^>]+id="[^"]*ViewState[^"]*"[^>]+value="([^"]+)"`,
	}

	for _, pattern := range patterns {
		re := regexp.MustCompile(pattern)
		matches := re.FindStringSubmatch(html)
		if len(matches) >= 2 {
			return matches[1], nil
		}
	}

	return "", fmt.Errorf("ViewState not found in HTML")
}

func extractFormAction(html, baseURL string) (string, error) {
	re := regexp.MustCompile(`<form[^>]+action="([^"]+)"`)
	matches := re.FindStringSubmatch(html)
	if len(matches) < 2 {
		return "", fmt.Errorf("form action not found")
	}

	formAction := matches[1]
	
	// Handle relative URLs
	if !strings.HasPrefix(formAction, "http") {
		baseURLObj, err := url.Parse(baseURL)
		if err != nil {
			return "", err
		}
		
		actionURL, err := url.Parse(formAction)
		if err != nil {
			return "", err
		}
		
		return baseURLObj.ResolveReference(actionURL).String(), nil
	}
	
	return formAction, nil
}

func extractFormId(html string) string {
	re := regexp.MustCompile(`<form[^>]+id="([^"]+)"`)
	matches := re.FindStringSubmatch(html)
	if len(matches) < 2 {
		return "form" // Default form id
	}
	return matches[1]
}

func extractDownloadButtonId(html string) string {
	// First look for the download button with specific text
	re := regexp.MustCompile(`<a[^>]+id="([^"]+)"[^>]*>.*?Download All Attachments.*?</a>`)
	matches := re.FindStringSubmatch(html)
	if len(matches) >= 2 {
		return matches[1]
	}
	
	// Fallback to default
	return "downloadAllAttachments"
}

func extractFilenameFromContentDisposition(header string) string {
	if header == "" {
		return ""
	}
	
	// Try filename="name.ext" format
	re := regexp.MustCompile(`filename="([^"]+)"`)
	matches := re.FindStringSubmatch(header)
	if len(matches) >= 2 {
		return matches[1]
	}
	
	// Try filename=name.ext format
	re = regexp.MustCompile(`filename=([^;]+)`)
	matches = re.FindStringSubmatch(header)
	if len(matches) >= 2 {
		return strings.TrimSpace(matches[1])
	}
	
	return ""
}
