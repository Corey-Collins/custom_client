#include <iostream>
#include "client.h"
#include <thread>
#include <future>
using namespace std;

Client::Client()
{
	cout << "A client has been made.\n";
	listenerOn = false;
	if(startListener() == 0)
		cout << "Listener started successfully.\n";
}

int Client::startListener()
{
	return 0;
}

int simplefunc(std::string a)
{ 
    return a.size();
}

int test()
{
      auto f = std::async(simplefunc, "hello world");
      int simple = f.get();
      return simple;
}

int main(int argc, char* argv[])
{
	Client client; 
	int x = test();
	cout << "this is a test" << endl;
	return 0;
}