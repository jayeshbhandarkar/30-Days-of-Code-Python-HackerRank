#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
    int n1, n2;
    
    cin >> n1;
    vector<int> numbers(n1);
    for (int i = 0; i < n1; i++) 
    {
        cin >> numbers[i];
    }

    cin >> n2;
    vector<string> words(n2);
    for (int i = 0; i < n2; i++)
    {
        cin >> words[i];
    }

    for (int i = 0; i < n1; i++) 
    {
        cout << numbers[i] << endl;
    }

    for (int i = 0; i < n2; i++) 
    {
        cout << words[i] << endl;
    }

    return 0;
}
