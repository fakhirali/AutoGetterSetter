#include <iostream>
using namespace std;

class Computer{
private:
	int price;
	int year;
	string name;
public:
	Computer(int p, int y){
		price = p;
		year = y;
	}
// setter
void setprice(int p){
	price = p;
}
// getter
int getprice(){
	return price;
}
// setter
void setyear(int y){
	year = y;
}
// getter
int getyear(){
	return year;
}
// setter
void setname(string n){
	name = n;
}
// getter
string getname(){
	return name;
}


};
