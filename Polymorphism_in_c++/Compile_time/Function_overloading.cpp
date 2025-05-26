
#include <iostream>
#define pi 3.14

int calculatePerimeter(int side1, int side2, int side3)
{
    //calculate perimeter for triangle
    return (side1 + side2 + side3);
}

int calculatePerimeter(int side1, int side2)
{
    //calculate perimeter for rectangle
    return 2 * (side1 + side2);
}


int calculatePerimeter(int radius)
{
    //calculate perimeter for circle
    return 2 * pi * radius;
}



int main()
{
    int triangle = calculatePerimeter(1, 2, 3);
    std::cout << triangle << std::endl;
    double circle = calculatePerimeter(6);
    std::cout << circle << std::endl;
    int rectangle = calculatePerimeter(5, 7);
    std::cout << rectangle << std::endl;

}
