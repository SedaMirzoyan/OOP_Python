#include <iostream>
#include <string>

template<typename T>

class Array {
private:
    T* m_ptr = nullptr;
    int m_size;
    int m_current_size;

public:
    Array();
    Array(int n);
    ~Array();
    Array(const Array& ob);
    Array(Array&& ob);
    Array& operator=(const Array& ob);
    Array& operator =(Array&& ob);
    T& operator[](int index) const;
    T& at(int index) const;
    bool operator >(const Array& ob);
    bool operator <(const Array& ob);
    bool operator ==(const Array& ob);
    T* genElements();
    T getElement(int index);
    void printArray();
    int getSize()const;
    int getCurrentSize()const;
    void pushBack(T elem);
    T popBack();
};

template <typename T>
Array<T>::Array<T>()
{
    std::cout << "Default " << __func__ << "\n";
    m_size = 0;
    m_current_size = 0;
}

template <typename T>
Array<T>::Array<T>(int n)
{
    std::cout << "Parametrized " << __func__ << "\n";
    m_size = n;
    m_current_size = n;
    m_ptr = new T[m_size];
}

template <typename T>
Array<T>::~Array()
{
    std::cout << __func__ << "\n";
    delete[] m_ptr;
}

template <typename T>
Array<T>::Array<T>(const Array& ob) :m_size(ob.m_size), m_current_size(ob.m_current_size) 
{
    std::cout << "Copy " << __func__ << "\n";

    this->m_ptr = new T[m_size];

    for (int i = 0; i < m_size; i++)
    {
        this->m_ptr[i] = ob.m_ptr[i];
    }
}


template <typename T>
Array<T>::Array<T>(Array&& ob) :m_size(ob.m_size), m_current_size(ob.m_current_size)
{
    std::cout << "Move " << __func__ << "\n";

    if (this != &ob)
    {
        this->m_ptr = ob.m_ptr;

        ob.m_ptr = nullptr;
        ob.m_size = 0;
    }
}

template <typename T>
Array<T>& Array<T>::operator=(const Array& ob)
{
    std::cout << __func__ << "\n";

    if (this != &ob)
    {
        std::cout << __func__ << "\n";
        this->m_size = ob.m_size;
        delete[] m_ptr;

        this->m_ptr = new T[this->m_size];

        for (int i = 0; i < m_size; i++)
        {
            this->m_ptr[i] = ob.m_ptr[i];
        }
    }
    return *this;
}


template <typename T>
Array<T>& Array<T>::operator =(Array&& ob)   //move operator assignment
{
    std::cout << "Move " << __func__ << "\n";

    if (this != &ob)
    {
        delete this->m_ptr;
        this->m_size = ob.m_size;

        this->m_ptr = ob.m_ptr;

        ob.m_ptr = nullptr;
        ob.m_size = 0;
    }
    return *this;
}

template <typename T>
T& Array<T>::operator[](int index) const
{
    return m_ptr[index];
}

template <typename T>
T& Array<T>::at(int index) const
{
    if (index < 0 || index >= m_size)
    {
        std::cout << "Out of range\n";
    }
    //std::cout << "Element with index " << index << " and with value " << ptr[index] << std::endl;
    return m_ptr[index];
}


template <typename T>
bool Array<T>::operator >(const Array& ob)
{
    bool flag = false;
    if (this->m_size > ob.m_size)
    {
        flag = true;
    }
    std::cout << std::boolalpha << flag << std::endl;
    return flag;
}


template <typename T>
bool Array<T>::operator <(const Array& ob)
{
    bool flag = false;
    if (this->m_size < ob.m_size)
    {
        flag = true;
    }
    std::cout << std::boolalpha << flag << std::endl;
    return flag;
}


template <typename T>
bool Array<T>::operator ==(const Array& ob)
{
    bool flag = false;
    if (this->m_size == ob.m_size)
    {
        flag = true;
    }
    std::cout << std::boolalpha << flag << std::endl;
    return flag;
}


template <typename T>
T* Array<T>::genElements()
{
    for (int i = 0; i < m_size; i++)
    {
        m_ptr[i] = rand() % 100 + 1;
    }
    return m_ptr;
}


template <typename T>
T Array<T>::getElement(int index)
{
    if (index > m_size || m_size < 0)
    {
        std::cout << "Out of range\n";
        //return -1;
    }
    else
    {
        std::cout << "Element with value " << m_ptr[index] << " was returned\n";
        //return m_ptr[index];           
    }
    return m_ptr[index];
}

template <typename T>
void Array<T>::printArray()
{
    for (int i = 0; i < m_size; i++)
    {
        std::cout << "element[" << i << "] = " << m_ptr[i] << std::endl;
    }
}


//size, pushBack, popBack
template <typename T>
int Array<T>::getSize()const
{
    return m_size;
}


template <typename T>
void Array<T>::pushBack(T elem)
{
    m_current_size = m_size+ 1;
    T* new_ptr = new T[m_current_size];

    for (int i = 0; i < m_current_size; i++)
    {
        new_ptr[i] = m_ptr[i];
    }
    new_ptr[m_current_size - 1] = elem;

    m_ptr = new T[m_current_size];

    for (int i = 0; i < m_current_size; i++)
    {
        m_ptr[i] = new_ptr[i];
    }
    m_size = m_current_size;
    delete[]new_ptr;
}


template <typename T>
T Array<T>::popBack()   
{
    T elem;

    if (m_size > 0)
    {
        elem = m_ptr[m_size - 1];
        this->m_size--;
        m_current_size = m_size;
    }
    else
    {
        throw std::logic_error("empty array");
    }
    
    return elem;
}


template <typename T>
int Array<T>::getCurrentSize()const
{
    return m_current_size;
}


int main()
{
    int n;
    std::cout << "Enter the number of elements\n";
    std::cin >> n;

    Array<int> ob(n);
    ob.genElements();
    ob.printArray();
    ob.getElement(2);

    ob[3];
    ob[2] = 45;
    std::cout << "After operator []\n";
    ob.printArray();

    std::cout << "At\n";
    ob.at(2);
    ob.at(1) = 8;
    ob.printArray();

    /*Array<int> ob_cp(ob);
    ob > ob_cp;

    Array<int> ob1;
    ob1 = ob_cp;
  
    Array<double> m_ob1(3);
    m_ob1 = std::move(Array<double>(5));   

    Array<std::string> m_ob2 = std::move(Array<std::string>(2)); */

    ob.pushBack(9);
    ob.printArray();
    std::cout << "after pushBack (current size is " << ob.getCurrentSize() << ")\n";
    ob.popBack();
    std::cout << "after popBack (current size = " << ob.getCurrentSize() << ")\n";
    ob.printArray();

    Array<int> ob_empty;
    try 
    {
        ob_empty.popBack();
    }
    catch (...)
    {
        std::cout << "Array is empty";
    }

    return 0;
}