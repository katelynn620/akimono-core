# �A�C�e���j�������� 2004/01/20 �R��

my $msg1="�j��";
my $msg2="�S��";
if ($ITEM[$itemno]->{flag}=~/h/)
	{
	$msg1="����";
	$msg2="�S��";
	}

$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="item-t">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=bk VALUE="$Q{bk}">
<INPUT TYPE=HIDDEN NAME=item VALUE="$itemno">
<BIG>��$msg1�F</BIG>
<SELECT NAME=cnt1>
<OPTION VALUE="0" SELECTED>
STR
	$stock=$DT->{item}[$itemno-1];
	$msg{1}=1;
	$msg{10}=10;
	$msg{100}=100;
	$msg{1000}=1000;
	$msg{10000}=10000;
	$msg{$stock}="$stock($msg2)";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1,10,100,1000,10000,$stock))
	{
		last if $stock<$cnt || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
$disp.=<<STR;
</SELECT>
$ITEM[$itemno]->{scale}�A��������
<INPUT TYPE=TEXT SIZE=5 NAME=cnt2>
$ITEM[$itemno]->{scale}
<INPUT TYPE=SUBMIT VALUE="$msg1����">(���ԏ��)
</FORM>
STR
1;
