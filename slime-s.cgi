# �h���S�����[�X���� 2005/03/30 �R��

$NOITEM=1;
$NOMENU=1;
CoLock();
DataRead();
CheckUserPass();
RequireFile('inc-dragon.cgi');

RequireFile("inc-dras-$Q{mode}.cgi");
CoUnLock();
OutSkin();
1;

