# ���|�� 2005/01/06 �R��

Lock();
DataRead();
CheckUserPass();

$time=int(GetStockTime($DT->{time})/ 3600);
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$time);
OutError('���Ԃ��w�肵�Ă�������') if ($count < 1);
my $usetime=GetTimeDeal($DT->{trush});
$usetime=$count * 3600 if ($usetime > $count * 3600);
my $deal=$count * 3600 / $TIME_SEND_MONEY * $TIME_SEND_MONEY_PLUS;
$deal=$DT->{trush} if ($DT->{trush} < $deal);

$DT->{trush}-=$deal;
UseTime($usetime);

RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>�����|�����|�[�g</BIG><br><br>���|�����s���܂����B<br><br>";
$disp.=$TB.$TR.$TD;
$disp.="<SPAN>�\\�菊�v����</SPAN>�F".$count."����<br>";
$disp.="<SPAN>���ۂ�����������</SPAN>�F".GetTime2HMS($usetime)."<br>";
$disp.="<SPAN>�ŏ����������݂̗�</SPAN>�F".int(($DT->{trush}+$deal)/10000)."kg<br>";
$disp.="<SPAN>�Еt�������݂̗�</SPAN>�F".int($deal/10000)."kg<br>";
$disp.="<SPAN>�c�������݂̗�</SPAN>�F".int($DT->{trush}/10000)."kg";
$disp.=$TRE.$TBE;

DataWrite();
DataCommitOrAbort();
UnLock();

OutSkin();
1;
