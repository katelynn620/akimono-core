# ���|�� 2004/01/20 �R��

DataRead();
CheckUserPass();
RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>�����|��</BIG><br><br>";

my $usetime=GetTimeDeal($DT->{trush})-$TIME_SEND_MONEY+3599;	#�[����؂�グ
my $time=int($usetime/3600);
my $stocktime=int(GetStockTime($DT->{time})/3600);

if($DT->{trush} < 10000)
{
	$disp.=$TB.$TR;
	$disp.=$TD.GetTagImgKao("���|���A�h�o�C�U","sweep").$TD;
	$disp.="���|���A�h�o�C�U�F���݂��X�ɖڗ��������݂͂���܂���B<br>";
	$disp.="�܂����݂����܂�����C���܂߂ɑ|�����܂��傤�B";
	$disp.=$TRE.$TBE;
HTML
}
else
{
	$disp.=$TB.$TR;
	$disp.=$TD.GetTagImgKao("���|���A�h�o�C�U","sweep").$TD;
	$disp.="���|���A�h�o�C�U�F����".int($DT->{trush}/10000)."kg�����̂��݂�����܂��ˁB<br>";
	$disp.="�����S���Еt����ɂ�".GetTime2found($usetime)."���炢�����肻���ł��B";
	$disp.=$TRE.$TBE;

	if ($stocktime < 1)
	{
	$disp.=<<"HTML";
	<br><BIG>�����Ԏw��F</BIG>���Ԃ�����܂���
HTML
	}
	else
	{
	$disp.=<<"HTML";
	<br><FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE=sweep-s>
	$USERPASSFORM
	<BIG>�����Ԏw��F</BIG>
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
HTML
	$msg{1}=1; $msg{2}=2; $msg{3}=3; $msg{5}=5; $msg{10}=10;
	$msg{$stocktime}="$stocktime(���ԍő�)";
	$msg{$time}="$time(�|���ő�)";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1,2,3,5,10,$time,$stocktime))
	{
		last if $time<$cnt || $stocktime<$cnt || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.=<<STR;
	</SELECT>
	���ԁA��������
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2>����
	<INPUT TYPE=SUBMIT VALUE="�|������"></FORM>
STR
	}
}

OutSkin();
1;
