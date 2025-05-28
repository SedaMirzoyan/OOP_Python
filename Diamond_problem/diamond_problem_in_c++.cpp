/**
* Diamond problem example
* Platypus is a mammal, but has mix of characteristics from reptiles, birds as well.
* In the following example Platypus inherits from both Mammal and Reptile classes.
*/

#include <iostream>
#include <string>

class Animal
{
public:
    virtual void display() = 0;

    Animal()
    {
        std::cout << "Animal constructor" << std::endl;
    }

    virtual ~Animal()
    {
        std::cout << "Animal destructor" << std::endl;
    }
};

class Mammal : virtual public Animal
{
private:
    std::string color;

public:
    void display()
    {
        std::cout << "display method from Mammal class" << std::endl;
    }

    Mammal()
    {
        std::cout << "Mammal constructor" << std::endl;
    }

    ~Mammal()
    {
        std::cout << "Mammal destructor" << std::endl;
    }
};

class Reptile : virtual public Animal
{
private:
    std::string color;

public:
    void display()
    {
        std::cout << "display method from Reptile class" << std::endl;
    }

    Reptile()
    {
        std::cout << "Reptile constructor" << std::endl;
    }

    ~Reptile()
    {
        std::cout << "Reptile destructor" << std::endl;
    }
};

class Platypus : public Mammal, Reptile
{
private:
    std::string color;

public:
    void display()
    {
        std::cout << "display method from Platypus class" << std::endl;
    }

    Platypus()
    {
        std::cout << "Platypus constructor" << std::endl;
    }

    ~Platypus()
    {
        std::cout << "Platypus destructor" << std::endl;
    }
};


int main()
{
    Platypus ob;
    ob.display();
}

