#ifndef __CLIENT_H_
#define __CLIENT_H_

class Client
{
public:
	Client();
	//~Client();

private:
	bool listenerOn;
	int startListener();
};

#endif