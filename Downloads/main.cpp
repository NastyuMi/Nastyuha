#include <iostream>
#include <string>
using namespace std;
int main()
{
setlocale(LC_ALL, "Russian");
string words[100];
string key;
int position = 0; int ans[20];
cout<<"argument- ";
cin>>key;
for (int i=0;i<7;i++){cin>>words[i];}
for (int i=0;i<7;i++){cout<<words[i]<<" ";}
cout<<endl;

  for (int i = 0; i < 20; i++)
   {if (words[i] == key)
        {ans[position++] = i;}}

  if (position !=0 && position<2 )
    { for (int i = 0; i < position; i++) {cout << "���� " << key << " ��������� � ������ " << ans[i] << endl; }}
  else if (position>1)
  { cout <<  key << " �� ����� �������� ������\n �.� �� ���������� ����� ������ ����" << endl;}
  else
  {cout << "������" << key << " ��� � ������";}
}
