
#include <iostream>

class A
{
private:
	int a;
public:
	A():a(0)
	{
		std::cout << __func__ << std::endl;
	}

	A(int n):a(n)
	{
		std::cout << __func__ << std::endl;
	}

	~A()
	{
		std::cout << __func__ << std::endl;
	}

	A operator++(int)	
	{
		A tmp(*this);
		this->a++;

		return tmp;
	}

	A& operator++() //++a
	{
		this->a++;

		return *this;
	}

	void print()
	{
		std::cout << "a = " << this->a << std::endl;
	}

};


int main()
{
	A ob(3);
	A ob1(3);

	std::cout << "ob_assign print\n";
	A ob_assign = ++ob;
	ob_assign.print();
	std::cout << "ob1_assign print\n";
	A ob1_assign = ob1++;
	ob1_assign.print();

	++ob;
	ob1++;

	std::cout << "ob print\n";
	ob.print();
	std::cout << "ob1 print\n";
	ob1.print();

	return 0;
}
