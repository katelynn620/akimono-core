# �X�ֈꗗ 2004/01/20 �R��

$NOMENU=1;
$Q{bk}="none";
$NOITEM=1;
DataRead();
CheckUserPass();
OutError("") if !$MASTER_USER;

ReadLetterName();
ReadLetter();

$disp.="<BIG>���X�փ`�F�b�N</BIG><br><br>";

foreach my $i(0..$Lcount)
	{
	my $sname=SearchLetterName($LETTER[$i]->{fromid},$LETTER[$i]->{fromt});
	$sname="(�s��)" if $sname eq "-1";
	my $tname=SearchLetterName($LETTER[$i]->{toid},$LETTER[$i]->{tot});
	$tname="(�s��)" if $tname eq "-1";
	$disp.="��";
	$disp.=($LETTER[$i]->{mode}==1) ? "<SPAN>����</SPAN>�F" : "���ǁF";
	$disp.=GetTime2FormatTime($LETTER[$i]->{time})." �c from�F<span>".$sname."</span>";
	$disp.=" <small>�i".$Tname{$LETTER[$i]->{fromt}}."�j</small> ";
	$disp.=" �c to�F<span>".$tname."</span>";
	$disp.=" <small>�i".$Tname{$LETTER[$i]->{tot}}."�j</small>";
	$disp.="<table width=75%><tr><td>";
	$disp.="�u".$LETTER[$i]->{title}."�v<BR>";
	$disp.=$LETTER[$i]->{msg}."<BR>";
	$disp.="</td></tr></table><hr width=500 noshade size=1>";
	}

OutSkin();
1;
