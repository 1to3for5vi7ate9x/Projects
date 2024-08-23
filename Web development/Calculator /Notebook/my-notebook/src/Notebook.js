import React, { useState } from 'react';
import { ChevronLeft, ChevronRight } from 'lucide-react';

const Notebook = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [currentPage, setCurrentPage] = useState(0);
  const [pages, setPages] = useState([{ content: '' }]);

  const addPage = () => {
    setPages([...pages, { content: '' }]);
    setCurrentPage(pages.length);
  };

  const updatePageContent = (content) => {
    const updatedPages = [...pages];
    updatedPages[currentPage].content = content;
    setPages(updatedPages);
  };

  const nextPage = () => {
    if (currentPage < pages.length - 1) {
      setCurrentPage(currentPage + 1);
    } else {
      addPage();
    }
  };

  const prevPage = () => {
    if (currentPage > 0) {
      setCurrentPage(currentPage - 1);
    }
  };

  return (
    <div className="flex flex-col items-center w-full max-w-2xl mx-auto" style={{ perspective: '1000px' }}>
      <div 
        className={`w-full h-[600px] bg-[#8B4513] rounded-lg shadow-lg overflow-hidden relative transition-all duration-1000 ${
          isOpen ? 'rotate-y-180' : ''
        }`}
        style={{ transformStyle: 'preserve-3d' }}
      >
        {/* Cover */}
        <div 
          className="absolute inset-0 bg-[#8B4513] rounded-lg shadow-inner flex items-center justify-center cursor-pointer"
          style={{ backfaceVisibility: 'hidden' }}
          onClick={() => setIsOpen(true)}
        >
          <h1 className="text-4xl font-bold text-[#FFD700]">My Notebook</h1>
        </div>

        {/* Notebook Pages */}
        <div 
          className="absolute inset-0 bg-yellow-100 rotate-y-180"
          style={{ backfaceVisibility: 'hidden' }}
        >
          <div className="absolute left-0 top-0 bottom-0 w-8 bg-yellow-200 shadow-inner"></div>
          <textarea
            className="w-full h-full p-8 pl-12 bg-yellow-100 text-gray-800 text-lg leading-relaxed resize-none focus:outline-none"
            value={pages[currentPage].content}
            onChange={(e) => updatePageContent(e.target.value)}
            placeholder="Start writing..."
          />
          <div className="absolute bottom-4 right-4 flex space-x-2">
            <button
              onClick={prevPage}
              disabled={currentPage === 0}
              className="p-2 bg-yellow-200 rounded-full shadow-md disabled:opacity-50"
            >
              <ChevronLeft size={24} />
            </button>
            <button
              onClick={nextPage}
              className="p-2 bg-yellow-200 rounded-full shadow-md"
            >
              <ChevronRight size={24} />
            </button>
          </div>
          <div className="absolute bottom-4 left-4 text-sm text-gray-600">
            Page {currentPage + 1} of {pages.length}
          </div>
        </div>

        {/* Page turn effect */}
        <div 
          className={`absolute inset-0 bg-yellow-100 shadow-md transition-transform duration-500 origin-left ${
            isOpen ? 'rotate-y-[-170deg]' : ''
          }`}
          style={{ backfaceVisibility: 'hidden' }}
        ></div>
      </div>
    </div>
  );
};

export default Notebook;