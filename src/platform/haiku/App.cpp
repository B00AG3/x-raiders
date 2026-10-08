#include "App.h"

const char* kApplicationSignature = "application/x-vnd.XProger-X-Raiders";


App::App()
	:
	BApplication(kApplicationSignature)
{
	MainWindow* mainWindow = new MainWindow();
	mainWindow->Show();
}


App::~App()
{
}
