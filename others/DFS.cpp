#include <stdio.h>
#define N 100 

FILE*in=fopen("in.txt","r");
FILE*out=fopen("out.txt","w");

int n, s, G[N][N], visited[N]; 

void DFS(int s){
    int i;
    visited[s]=1;
    fprintf(out, "%d ", s);
    for(i=1;i<=n;i++) {
    if(G[s][i]==1 && visited[i]!=1)
        DFS(i);
    }
}



int main() { 
    int x,y; 
    
    fscanf(in,"%d %d", &n, &s); 
    
    while(fscanf(in,"%d %d",&x,&y)!=EOF) 
        G[x][y]=G[y][x]=1;
        
    DFS(s); 
    fclose(in); 
    fclose(out); 
    return 0; 
}
