# �̎�{�� 2005/01/06 �R��

$image[0]=GetTagImgKao("��b","minister");
DataRead();
CheckUserPass();
OutError('�������s����̂͗̎�݂̂ł�') if $STATE->{leader}!=$DT->{id};

my $shoplist="";
my $taxsum=0;
foreach (@DT) {
$shoplist.="<OPTION VALUE=\"$_->{id}\">$_->{shopname}";
$taxsum+=$_->{taxtoday};
}

my $now=$DTlasttime+$TZ_JST-$DATE_REVISE_TIME;
my $ii=($now % $ONE_DAY_TIME);
$ii=1 if $ii < 1;
$taxsum=GetMoneyString(int($taxsum * $ONE_DAY_TIME / $ii / 10000) * 10000);

$disp.="<BIG>��������</BIG><br><br>";
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>��b</SPAN>�F����͂���͗̎�l�B���@������킵�イ�������܂��B<br>";
$disp.="�����̂��ƂȂǑ�b�ɂ��C����������΂����̂ɁC���M�S�ł��ȁB�ӂ�B".$TRE.$TBE;
my $money=GetMoneyString($STATE->{money}+0);
my $army=$STATE->{army} + $STATE->{robina};
my $armycost=200-int($STATE->{safety} / 100); 	# 100 - 200
my $armyc=GetMoneyString($STATE->{army} * $armycost);

$disp.=<<"HTML";
<hr width=500 noshade size=1><BIG>�������ݒ�</BIG><br><br>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="lord-s">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="inside">
$TB$TDB�X����$TDB�Ŏ�������$TDB�ŗ�
$TDB�J��΍���$TDB�����΍���$TRE
$TR$TD<b>$money</b>
$TD$taxsum
$TD<INPUT TYPE=TEXT NAME=taxrate SIZE=5 VALUE="$DTTaxrate"> %<br><small>(�W�� 20%)</small>
$TD$term[0]<INPUT TYPE=TEXT NAME=devem SIZE=10 VALUE="$STATE->{devem}">$term[1]<br><small>(�W�� $term[0]5,000,000$term[1])</small>
$TD$term[0]<INPUT TYPE=TEXT NAME=safem SIZE=10 VALUE="$STATE->{safem}">$term[1]<br><small>(�W�� $term[0]5,000,000$term[1])</small>
$TRE$TBE
<br><INPUT TYPE=SUBMIT VALUE="�ȏ�̓��e�Ō���">
</FORM>

<hr width=500 noshade size=1><BIG>���ܔ�</BIG><br><br>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="lord-s">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="taxside">
<BIG>���ʐŗ�</BIG>�F 
<SELECT NAME=tg>$shoplist</select>
 �̐ŗ���
<SELECT NAME=md><OPTION VALUE="normal">�ʏ�
<OPTION VALUE="free">�Ə�
<OPTION VALUE="double">�Q�{
</select> �� <INPUT TYPE=SUBMIT VALUE="�ݒ肷��">
</FORM>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="lord-s">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="treset">
<BIG>���ŗ����Z�b�g</BIG>�F 
���ׂĂ̓X�̐ŗ��� �ʏ� �� <INPUT TYPE=SUBMIT VALUE="���Z�b�g����">
</FORM>
HTML

if ($DTevent{rebel})
{
$disp.="<BIG>���X�܎����܂�</BIG>�F �������̂��ߎ��s�ł��܂���";
}
elsif ($STATE->{army} < 2000)
{
$disp.="<BIG>���X�܎����܂�</BIG>�F �����܂�ɕK�v�ȕ��m��������܂���";
}
elsif ($STATE->{money} < 1000000)
{
$disp.="<BIG>���X�܎����܂�</BIG>�F ��p������܂���";
}
else
{
$disp.=<<"STR";
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="lord-s">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="expose">
<BIG>���X�܎����܂�</BIG>�F 
<SELECT NAME=tg>$shoplist</select>
 ���R���� 
 <INPUT TYPE=SUBMIT VALUE="�����܂�"> (��p$term[0]1,000,000$term[1])
</FORM>
STR
}

$disp.=<<"HTML";
<hr width=500 noshade size=1><BIG>���R���ݒ�</BIG><br><br>
$TB$TR$TDB���݂̕���
$TD<b>$army�l</b><small>�i���K�R $STATE->{army}�l�C�`�E�R $STATE->{robina}�l�j$TRE
$TR$TDB���͈ێ���
$TD<b>$armyc</b><small>�i���K�R�P�l�ɂ�$term[0]$armycost$term[1]�j$TRE
$TBE
HTML

if ($STATE->{money}>0 && !$DTevent{rebel})
{
	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="lord-s">
	$USERPASSFORM
	<INPUT TYPE=hidden NAME=mode VALUE="outside">
	<BIG>�����͑���</BIG>�F ���m�� 
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	my $stock=int($STATE->{money} / 1200);
	$msg{1000}=1000;
	$msg{5000}=5000;
	$msg{10000}=10000;
	$msg{20000}=20000;
	$msg{$stock}="$stock(�����ő�)";
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
	<INPUT TYPE=SUBMIT VALUE="��������"> @$term[0]1,200$term[1]
	</FORM>
STR
	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="lord-s">
	$USERPASSFORM
	<INPUT TYPE=hidden NAME=mode VALUE="outdel">
	<BIG>�����͍팸</BIG>�F ���m�� 
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	my $army=$STATE->{army}+0;
	$msg{1000}=1000;
	$msg{5000}=5000;
	$msg{10000}=10000;
	$msg{20000}=20000;
	$msg{$army}="$army(���m�ő�)";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1000,5000,10000,20000,$army))
	{
		last if $army<$cnt || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.=<<STR;
	</SELECT>
	 �l�A�������� 
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2> �l
	<INPUT TYPE=SUBMIT VALUE="���ق���"> @$term[0]0$term[1]
	</FORM>
STR
}

OutSkin();
1;
