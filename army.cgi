# ���m���ԏ� 2005/01/06 �R��

$image[0]=GetTagImgKao("�ē��l","army");
DataRead();
CheckUserPass();
ReadArmy();
RequireFile('inc-html-ownerinfo.cgi');

my $price=($DTevent{rebel}) ? 1500 : 1000;
my $level=DignityDefine($DT->{dignity},2);
$level=$DIGNITY[0] if !$level;

$disp.="<BIG>���b����</BIG><br><br>";
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>�ē��l</SPAN>�F�����ɂ̓h���[�t���������ق�������߂ďW�܂��Ă��܂��B<br>";
$disp.="�ނ���W�߂Ĕ������N�������C�t�ɗ̎�������C�ق��原��ł��B".$TRE.$TBE;

$disp.="<hr width=500 noshade size=1><BIG>��$DT->{shopname}�̌ٗp��</BIG><br><br>";
$disp.="$TB$TR$TDB�݈�$TD$level <small>(�o���l ".($DT->{dignity}+0)."pt)$TRE";
$disp.="$TR$TDB�ٗp�ő吔$TD".(($DT->{dignity}+0)*1000)."�l$TRE";
$disp.="$TR$TDB�ٗp��p$TD@".GetMoneyString($price)."$TRE";
$disp.="$TR$TDB�ٗp��$TD".($ARMY{$DT->{id}}+0)."�l$TRE";
$disp.="$TR$TDB���$TD".($RIOT{$DT->{id}} ? "<SPAN>����</SPAN>" : "�ҋ@").$TRE;
$disp.=$TBE;

ArmyBuy();
if ($ARMY{$DT->{id}})
	{
	ArmyFire();
	ArmyRebel() if !$DTevent{rebel};
	ArmyAction() if $DTevent{rebel} && !$RIOT{$DT->{id}};
	}
OutSkin();
1;


sub ArmyBuy
{
my $usetime=60*40;
my $limit= ($DT->{dignity}+0)*1000 - $ARMY{$DT->{id}};
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>�����m�ٗp</BIG>�F���m���ق��ɂ͎݈ʂ��グ��K�v������܂�<BR>',return if $limit <= 0;
$disp.='<BIG>�����m�ٗp</BIG>�F����������܂���<BR>',return if $DT->{money}<$price;
$disp.='<BIG>�����m�ٗp</BIG>�F���Ԃ�����܂���<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="plus">
	<BIG>�����m�ٗp</BIG>�F ���m�� 
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	$money=int($DT->{money}/$price);
	$msg{1000}=1000;
	$msg{5000}=5000;
	$msg{10000}=10000;
	$msg{20000}=20000;
	$msg{$limit}="$limit(�ٗp�ő�)";
	$msg{$money}="$money(�����ő�)";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1000,5000,10000,20000,$limit,$money))
	{
		last if $cnt>$money || $cnt>$limit || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.=<<STR;
	</SELECT>
	 �l�A�������� 
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2> �l
	<INPUT TYPE=SUBMIT VALUE="�ٗp����">
STR
	$disp.="(�����:".GetTime2HMS($usetime).")</FORM>";
}


sub ArmyFire
{
my $usetime=60*10;
my $stock=($ARMY{$DT->{id}}+0);
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>�����m����</BIG>�F���Ԃ�����܂���<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="fire">
	<BIG>�����m����</BIG>�F ���m�� 
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	$msg{1000}=1000;
	$msg{5000}=5000;
	$msg{10000}=10000;
	$msg{20000}=20000;
	$msg{$stock}="$stock(���m�ő�)";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1000,5000,10000,20000,$stock))
	{
		last if $stock<$cnt || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.=<<STR;
	</SELECT>
	 �l�A�������� 
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2> �l
	<INPUT TYPE=SUBMIT VALUE="���ق���">
STR
	$disp.="(�����:".GetTime2HMS($usetime).")</FORM>";
}


sub ArmyRebel
{
return if ($STATE->{leader}==$DT->{id});
my $usetime=60*30;
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>�������I�N</BIG>�F�����ɕK�v�ȕ��m��������܂���B<BR>',return if ($ARMY{$DT->{id}} < 2500);
$disp.='<BIG>�������I�N</BIG>�F���Ԃ�����܂���<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="rebelon">
	<BIG>�������I�N</BIG>�F 
	<INPUT TYPE=TEXT NAME=cmd SIZE=10 VALUE="">
	(rebel �Ɠ���)
	������ <INPUT TYPE=SUBMIT VALUE="�J�n����">
STR
	$disp.="(�����:".GetTime2HMS($usetime).")</FORM>";
}


sub ArmyAction
{
my $usetime=60*20;
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>����������</BIG>�F���Ԃ�����܂���<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="rside">
	<BIG>����������</BIG>�F 
	<INPUT TYPE=TEXT NAME=cmd SIZE=10 VALUE="">
	(rebel �Ɠ���)
	������ <INPUT TYPE=SUBMIT VALUE="�ĉ�����">
STR
	$disp.="(�����:".GetTime2HMS($usetime).")</FORM>";

$usetime=60*20;
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>����q����</BIG>�F���Ԃ�����܂���<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="lside">
	<BIG>����q����</BIG>�F 
	���m��̎�̌�q�R�� <INPUT TYPE=SUBMIT VALUE="�h������">
STR
	$disp.="(�����:".GetTime2HMS($usetime).")</FORM>";
}
