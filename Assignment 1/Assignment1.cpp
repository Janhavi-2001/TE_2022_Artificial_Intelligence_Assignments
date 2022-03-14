#include <iostream>
#include <stack>
#include <queue>
#include <vector>
using namespace std;

void edge(vector<int>adj[], int u, int v)
{
    adj[u].push_back(v);                                    // constructing the edges of an undirected graph
}

void BFS(int s, vector<int>adj[], bool visited[])           // BFS uses a queue for it's implementation
{
    queue<int> q;
    q.push(s);                                              // inserting the first node into the queue
    visited[s] = true;                                      // marking the value as visited
    while(!q.empty())
    {
        int temp = q.front();
        cout << temp << " ";                                // printing the first node of the graph as it is
        q.pop();                                            // removing the first node from the queue

        for(int i=0;i<adj[temp].size();i++)                 // the process continues with the remaining nodes of the graph
        {
            if(!visited[adj[temp][i]])                      // checking to see whether the node has already been visited or not
            {
                q.push(adj[temp][i]);                       // pushing the element not visited into the queue
                visited[adj[temp][i]] = true;               // marking the node as a visited node 
            }
        }
    }
}


void DFS(int x, vector<int> adj[], bool visited[])          // DFS uses a stack for it's implementation
{
    stack<int> s;
    s.push(x);                                              // inserting the first node into the stack
    visited[x] = true;                                      // marking the value as visited
    while(!s.empty())
    {
        int temp = s.top();
        cout << temp << " ";                                // printing the first node of the graph as it is
        s.pop();                                            // removing the first node from the stack

        for(int i=0;i<adj[temp].size();i++)                 // the process continues with the remaining nodes of the graph
        {
            if(!visited[adj[temp][i]])                   // checking to see whether the node has already been visited or not
            { 
                s.push(adj[temp][i]);                    // pushing the element not visited into the stack
                visited[adj[temp][i]] = true;           // marking the node as a visited node
            }
        }
    }
}


int main()
{
    char choice;
    while(true)
    {
        cout << "Do you want to continue? (y/n): ";
        cin >> choice;
        if(choice == 'y')
        {
            int n;
            cout << "Enter the size of the adjacency list: ";
            cin >> n;

            vector<int>adj[n];                                      // initializing the adjacency list
            bool visited[n];                                        // initializing the visited array

            for(int i=0;i<n;i++)
            {
                visited[i] = false;                                 // initializing all array values to 'false'
            }
            int u;
            int v;
            cout << "Enter graph edges: " << endl;
            for(int i=0;i<n;i++)
            {
                cin >> u >> v;
                edge(adj, u, v);
            }

            cout << "********** MENU **********" << endl;
            cout << endl;
            cout << " 1. BFS " << endl;
            cout << " 2. DFS " << endl;
            cout << endl;
            cout << "**************************" << endl;
            cout << endl;
            char ch;
            cout << "Enter choice of operation: ";
            cin >> ch;

            if(ch == '1')
            {
                cout << "BFS traversal is: " << " ";                  
                BFS(0,adj,visited);                                     // calling the BFS function defined above
                cout << endl;
            }

            else if(ch == '2')
            {
                cout << "DFS traversal is: " << " ";
                DFS(0,adj,visited);                                     // calling the DFS function defined above
                cout << endl;
            }
            else
            {
                cout << "Please enter a valid option!" << endl;
            }
        }

        else
        {
            cout << "Bye" << endl;
            break;
        }
    }
    return 0;
}