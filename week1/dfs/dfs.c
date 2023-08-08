#include <stdio.h>
#include <stdlib.h>

#define n 5 // number of nodes

int visited[n] = {0, 0, 0, 0, 0};

int A[n][n] = {
    {0, 1, 1, 0, 0},
    {1, 0, 1, 1, 0},
    {1, 1, 0, 1, 0},
    {0, 1, 1, 0, 1},
    {0, 0, 0, 1, 0}
};
    /*
    
        1 ----- 2
        |     / |
        |    /  |
        |   /   |
        |  /    |
        | /     |
        3 ------4
                | 
                | 
                |
                5 
    */
void DFS(int i) {
    printf("%d ", i + 1); 
    visited[i] = 1;
    for (int j = 0; j < n; j++) {
        if (A[i][j] == 1 && !visited[j]) {
            DFS(j);
        }
    }
}

int main() {
    printf("\n\n");
    printf("DFS Traversal: ");
    DFS(0);
    printf("\n\n");
    return 0;
}
