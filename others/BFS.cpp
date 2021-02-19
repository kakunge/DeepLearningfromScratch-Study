#include <stdio.h>
#define N 100

FILE*in=fopen("in.txt","r");
FILE*out=fopen("out.txt","w");

int n, s,G[N][N],visited[N];
int Q[N], rear, front = 1;

bool Q_empty(){
    if(rear<front) return true;
    else return false;
}

int Q_top(){ return Q[front];}

void Q_pop(){front++;}

void Q_push(int s){
    rear++;
    Q[rear]=s;
}

void BFS()
{
    int i;
    Q_push(s);
    visited[s]=1;
    while(!Q_empty())
    {
        s=Q_top();
        fprintf(out, "%d ", s);
        Q_pop();
        for(i=1;i<=n;i++)
        {
            if(G[s][i]==1 && visited[i]!=1)
            {
                Q_push(i);
                visited[i]=1;
            }
        }
    }
}

int main()
{
    int x,y;
    fscanf(in, "%d %d",&n,&s);
    
    while(fscanf(in,"%d %d",&x,&y)!=EOF)
        G[x][y]=G[y][x]=1;
    
    BFS();
    
    fclose(in);
    fclose(out);
    return 0;
}
