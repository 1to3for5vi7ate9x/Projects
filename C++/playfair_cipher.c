#include<stdio.h>
#include<string.h>
int main()
{
char p[30],k[30],mat[5][5],out[30];
int pl,kl,cnt=0,ascii=97,bol=0,x,i,j,k1,k2,r,r1,cc,index=0,c1,rr,b;
printf("\n enter plain text: ");
scanf("%s",&p);
printf("\n enter key: ");
scanf("%s",&k);
pl=strlen(p);
kl=strlen(k);
//form a matrix of 5 by 5
printf("\n 5x5 matrix is:\n");
for(i=0;i<5;i++){
for(j=0;j<5;j++){
label: {
if(cnt<kl){
for(k1=0;k1<cnt;k1++){
//if key contains 'i' and 'j'
if(k[k1]==105 || k[k1]==73){
if(k[cnt]==k[k1] ||k[cnt]==k[k1]+1)
bol=1;
}
if(k[k1]==106 || k[k1]==74){
if(k[cnt]==k[k1] || k[cnt]==k[k1]-1)
bol=1;
}
if(k[k1]==k[cnt])
bol=1;
}
if(bol!=1){
mat[i][j]=k[cnt];
printf("\t %c", mat[i][j],"\n");
cnt++;
}
else{
cnt++;
bol=0;
goto label;
} }
else{
for(k2=0;k2<kl;k2++){
if(ascii==105 || ascii==73){
if(k[k2]==ascii || k[k2]==ascii+1)
bol=1;
}
if(ascii==106 || ascii==74){
if(k[k2]==ascii || k[k2]==ascii-1)
bol=1;
}
if(k[k2]==ascii)
bol=1;
}
if(bol!=1){
mat[i][j]=ascii;
printf("\t %c",mat[i][j],"\n");
if(ascii=='i')
ascii=ascii+2;
else
ascii++;
cnt++;
}
else{
if(ascii=='i')
ascii=ascii+2;
else
ascii++;
cnt++;
bol=0;
goto label;
} }
} }
printf("\n");
}
printf("\n formatted plain text is: ");
char sp[60];
int l=0;
for(i=0;i<pl;){
//add filler in middle as well as at end
if(p[i+1]==NULL){
sp[l]=p[i];
printf("%c",sp[l]);
l++;
sp[j]='X';
printf("%c",sp[l]);
i++;
l++;
}
else if(p[i]==p[i+1]){
sp[l]=p[i];
printf("%c",sp[l]);
l++;
sp[l]='X';
printf("%c",sp[l]);
i++;
l++;
}
else{
sp[l]=p[i];
printf("%c",sp[l]);
l++;
sp[l]=p[i+1];
printf("%c",sp[l]);
l++;
i=i+2;
}
}
printf("\n");
printf("%d",l);
printf("\n encrypted text is:");
for(b=0;b<l;b=b+2){
for(i=0;i<5;i++){
    for(j=0;j<5;j++){
//chek if j is there in plaintext or not
if(mat[i][j]==sp[b] || sp[b]=='j'){
if(sp[b]=='j'){
if(mat[i][j]=='i'){
r=i;
cc=j;
}
}
else{
r=i;
cc=j;
}
}
if(mat[i][j]==sp[b+1] || sp[b+1]== 'j'){
if(sp[b+1]=='j'){
if(mat[i][j]=='i'){
r1=i;c1=j;
}
}
else{
r1=i;c1=j;
}
}}}
//if row are same
if(r==r1){
//if its a last coloum
if(cc==4){
out[index]=mat[r][0];
printf("%c",out[index]);
index++;
}
else{
out[index]=mat[r][cc+1];
printf("%c",out[index]);
index++;
}
if(c1==4){
out[index]=mat[r1][0];
printf("%c",out[index]);
index++;
}
else{
    out[index]=mat[r1][c1+1];
printf("%c",out[index]);
index++;
}
}
//if coloumn are same
else if(cc==c1){
//if its a last row
if(r==4){
out[index]=mat[0][cc];
printf("%c",out[index]);
index++;
}
else{
out[index]=mat[r+1][cc];
printf("%c",out[index]);
index++;
}
if(r1==4){
out[index]=mat[0][c1];
printf("%c",out[index]);
index++;
}
else{
out[index]=mat[r1+1][c1];
printf("%c",out[index]);
index++;
}
}
else{
out[index]=mat[r][c1];
printf("%c",out[index]);
index++;
out[index]=mat[r1][cc];
printf("%c",out[index]);
index++;
}
}
return 0;
}

