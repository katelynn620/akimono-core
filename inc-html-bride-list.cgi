# �Z��� 2005/01/06 �R��

$i=SearchBride($Q{no});
OutError('�w�肳�ꂽ���͑��݂��܂���') if ($i==-1);
($ida,$idb)=($BRIDE[$i]->{ida},$BRIDE[$i]->{idb});

if (!$BRIDE[$i]->{mode})
{
Agree();
}
elsif ($Q{d})
{
DivCheck();
}
else
{
House();
}
1;

sub Agree
{
if ($idb == $DT->{id}) {
	# �v���|�[�Y����
	$disp.=<<STR;
$TB$TR$TD
$image[3]
�_���F�v���|�[�Y���󂯂܂����H ����Ȃ玟�̒��ӂ��悭�����Ă��������B<br>
�E����������<b>500��$term[2]</b>������܂��B<br>
�E���O�ɂ悭�b�������Ȃ����B���̐l�Ə��������Ă����邩�悭�l���Ȃ����B<br>
�E�v���|�[�Y�����������v�ƂȂ�C�󂯂������ȂɂȂ�܂��B
$TRE$TBE
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="agree">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<BIG>���v���|�[�Y���󂯂�</BIG>�F�� $DT->{name} ($DT->{shopname})��
$DT[$id2idx{$ida}]->{name} ($DT[$id2idx{$ida}]->{shopname})��v�Ƃ�<br>
���₩�Ȃ鎞���a�߂鎞�����̐g�����ɂ��鎖��
<INPUT TYPE=SUBMIT VALUE='�����܂�'>
</FORM>
<hr width=500 noshade size=1>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="dis">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<BIG>���v���|�[�Y��f��</BIG>�F����Ȃ��ƌ����Ă�����̂�
<INPUT TYPE=SUBMIT VALUE='���߂�Ȃ���'>
</FORM>
STR
}
elsif ($ida == $DT->{id}) {
	# �v���|�[�Y�P��
	$disp.=<<STR;
$TB$TR$TD
$image[3]
�_���F�v���|�[�Y������߂����ł����B<br>
�����p����������������܂��񂪎d������܂���ˁB
$TRE$TBE
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="end">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<BIG>���v���|�[�Y������߂�</BIG>�F��͂�܂���������Ȃ������̂�
<INPUT TYPE=SUBMIT VALUE='����߂܂�'>
</FORM>
STR
}
else {
	# �쎟�n
	$disp.=<<STR;
$TB$TR$TD
$image[3]
�_���F<b>$DT[$id2idx{$ida}]->{name}</b>�����
<b>$DT[$id2idx{$idb}]->{name}</b>����֑z���͐^���ł��B���Ԃ�B<br>
���͓�l������������������Ă����Ă��������B
$TRE$TBE
STR
}
}

sub House
{
$disp.=($BRIDE[$i]->{mode}==1)?$image[0]:$image[1];
$btitle=($BRIDE[$i]->{mode}==1)?"���� > ���p�q��":"�Z��";
	# ���֌W�Ȑl
	if ($DT->{id} != $ida && $DT->{id} != $idb) {
	$disp.=<<STR;
�F<BIG>$DT[$id2idx{$ida}]->{shopname} �� $DT[$id2idx{$idb}]->{shopname}</BIG><br><br>
$TB$TR$TD
��������ƁC�}�C�z�[���Ƃ��ē�l�̋��p�q�ɂ����炦�܂��B<br>
�����⏤�i��u�����Ƃ��ł��C�ێ����������܂���B
$TRE$TBE
STR
	return;
	}
	my $moneymes=GetMoneyString($BRIDE[$i]->{money});
	my $moneymax=GetMoneyString($BRIDE[$i]->{mode}*20000000);
	$disp.=<<STR;
�F<BIG>$DT[$id2idx{$ida}]->{shopname} �� $DT[$id2idx{$idb}]->{shopname}</BIG><br><br>
$TB$TR
$TDB���i
$TDB����<small>/�ő�</small>
$TRE
$TR$TD����
$TD$moneymes<small>/$moneymax</small>
$TRE
STR

$formstock="<OPTION VALUE=\"-1\">����(".GetMoneyString($BRIDE[$i]->{money}).")";
foreach (0..$BRIDE[$i]->{mode}-1) {
	my $stock=$BRIDE[$i]->{stock}[$_];
	my $cnt=$BRIDE[$i]->{cnt}[$_];
	$disp.='<tr><td>';
	$disp.=GetTagImgItemType($stock).$ITEM[$stock]->{name}.'<td>';
	$disp.=($cnt) ? ($cnt.'<small>/'.($ITEM[$stock]->{limit}*$HouseMax).$ITEM[$stock]->{scale}) : ' ';
	$formstock.="<OPTION VALUE=\"$_\">$ITEM[$stock]->{name}($cnt$ITEM[$stock]->{scale})" if ($cnt);
	}
$disp.=$TRE.$TBE."<hr width=500 noshade size=1>";

	my @sort;
	foreach(1..$MAX_ITEM){$sort[$_]=$ITEM[$_]->{sort}};
	my @itemlist=sort { $sort[$a] <=> $sort[$b] } (1..$MAX_ITEM);
	$formitem="<OPTION VALUE=\"-1\">����(".GetMoneyString($DT->{money}).")";
	foreach(@itemlist)
	{
		my $cnt=$DT->{item}[$_-1];
		$cnt=0 if ($ITEM[$_]->{flag}=~/r/);	# �˗��ł��Ȃ��A�C�e���͒u���Ȃ��B
		my $scale=$ITEM[$_]->{scale};
		$formitem.="<OPTION VALUE=\"$_\">$ITEM[$_]->{name}($cnt$scale)" if $cnt;
	}

$disp.=<<STR;
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=no VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=mode VALUE="plus">
<BIG>���ۊ�</BIG>�F�Z��� <SELECT NAME=it SIZE=1>
$formitem
</SELECT> �𐔗� <INPUT TYPE=TEXT NAME=num SIZE=5> (���L���ōő�)
 <INPUT TYPE=SUBMIT VALUE='�ۊǂ���'>
</FORM>
<hr width=500 noshade size=1>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=no VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=mode VALUE="minus">
<BIG>����o</BIG>�F�Z��� <SELECT NAME=it SIZE=1>
$formstock
</SELECT> �𐔗� <INPUT TYPE=TEXT NAME=num SIZE=5> (���L���ōő�)
 <INPUT TYPE=SUBMIT VALUE='���o��'>
</FORM>
STR

Reform() if ($BRIDE[$i]->{mode} > 2 && $BRIDE[$i]->{mode} < 7);

$disp.=<<STR;
<hr width=500 noshade size=1>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=no VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=d VALUE="1">
<SPAN>����</SPAN>�F
<INPUT TYPE=SUBMIT VALUE='��������'>
(���i�͑S�Ĕj��)
</FORM>
STR
}

sub Reform
{
if ($BRIDE[$i]->{money} > $BRIDE[$i]->{mode} * 10000000)
	{
$disp.=<<STR;
<hr width=500 noshade size=1>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=no VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=mode VALUE="more">
<BIG>�����z</BIG>�F
<INPUT TYPE=SUBMIT VALUE='���z����'>
STR
$disp.="(��p".GetMoneyString($BRIDE[$i]->{mode} * 10000000).")</form>";
	}
	else
	{
$disp.=<<STR;
<hr width=500 noshade size=1>
<BIG>�����z</BIG>�F����������܂���
STR
	}
}

sub DivCheck
{
	# �����m�F
	$disp.=<<STR;
$TB$TR$TD
$image[3]
�_���F�{���ɗ�������̂ł��ˁH
$TRE$TBE
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=mode VALUE="divorce">
<SPAN>������</SPAN>�F
<INPUT TYPE=SUBMIT VALUE='��������'>
(���i�͑S�Ĕj��)
</FORM>
STR
}
