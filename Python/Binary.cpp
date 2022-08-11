#include<iostream>
using namespace std ;
#define n 10
int arr[n] ;
void Search(int key ) {
    int mid , l = 0 , r = n-1 ;
    mid = (l+ r) /2;

    while (l == r)
    {
        if(arr[mid] ==  key) {
            cout << "The index is : "  << mid << endl;
        }
        else if(arr[mid] > key){
            
        }
    }
    



}
int main(){



    return 0 ;
}