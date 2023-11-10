#include <windows.h>
#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
    const wchar_t *file = L"C:\\Users\\andyy\\VSCodeProjects\\wallpaper\\picture.png";
    int ret = SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, (void *)file, SPIF_UPDATEINIFILE);
    cout<<ret<<endl;
    return 0;
}   