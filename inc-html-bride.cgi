# �Z��ꗗ�\�� 2005/03/30 �R��

if ($Q{form} eq "pro" && !$GUEST_USER)
{
ProposeForm();
}
elsif ($Q{form} && !$GUEST_USER)
{
ConstForm();
}
else
{
BrideList();
}
1;

sub BrideList
{
my $i;
if (!$GUEST_USER && !$married)
{
$i="<br><a href=\"action.cgi?key=bride&form=pro&$USERPASSURL\">[�v���|�[�Y����]</a>";
}

$disp.=<<STR;
$TBT$TRT$TD
<IMG width="96" height="192" SRC="$IMAGE_URL/map/church.png"><td width=10>$TD
$image[3]
<SPAN>�_��</SPAN><br>
�����ɂ��Ă����m�ł����H<br>
�������ďZ������Ă�ƁC�����Ɏ�������u�����Ƃ��ł���̂ł���B<br>
�Z������܂ł̊Ԃ́C���̋���̎������u������g���Ă��܂��܂���B<br>
�ł��厖�Ȃ̂́C��͂��l�̋����J�ł��傤�ˁB$i
$TRE$TBE<br>
$TB$TR
$TDB�_��
$TDB���
$TDB�ڍ�
$TDB����
$TDB�ۊǕi
$TRE
STR
@BRIDE=sort{$b->{point}<=>$a->{point}}@BRIDE;
foreach my $i(0..$Scount) {
	next if ($BRIDE[$i]->{mode}==-1) || !defined($BRIDE[$i]->{no});
	my ($ida,$idb)=($BRIDE[$i]->{ida},$BRIDE[$i]->{idb});
	$disp.=($DT->{id} == $ida || $DT->{id} == $idb) ? $TR.$TDB : $TR.$TD;
	$disp.='<b>No.'.($i+1).'</b><br>'.$BRIDE[$i]->{point}.'<td>';
	$disp.=    "<a href=\"action.cgi?key=bride&no=$BRIDE[$i]->{no}&$USERPASSURL\">" if (!$GUEST_USER);

	if (!$BRIDE[$i]->{mode})
	{
	$disp.=$image[2];
	$disp.=    "</a>" if (!$GUEST_USER);
	$disp.='<td>'.$DT[$id2idx{$ida}]->{shopname}.' ���� <SPAN>'.$DT[$id2idx{$idb}]->{shopname}."</SPAN> ��";
	}
	else
	{
	$disp.=($BRIDE[$i]->{mode}==1)?$image[0]:$image[1];
	$disp.=    "</a>" if (!$GUEST_USER);
	$disp.='<td>'.$DT[$id2idx{$ida}]->{shopname}.' �� '.$DT[$id2idx{$idb}]->{shopname};
	}
	$disp.="<td align=center>".GetTime2found($NOW_TIME-$BRIDE[$i]->{tm});
	$disp.='<td>'.GetMoneyMessage($BRIDE[$i]->{money}).'<br>';
	foreach (0..$BRIDE[$i]->{mode}-1) { $disp.=GetTagImgItemType($BRIDE[$i]->{stock}[$_]);}
	}
$disp.=$TRE.$TBE;
}

sub ProposeForm
{
	OutError("bad request") if $married;
	$userselect="";
	foreach my $DTS (@DT)
	{
		$userselect.="<OPTION VALUE=\"$DTS->{id}\">$DTS->{name} ($DTS->{shopname})";
	}
$disp.=<<STR;
$TB$TR$TD
$image[3]
�_���F�Ƒ��������Ƃ����]�݂ł����H ����Ȃ玟�̒��ӂ��悭�����Ă��������B<br>
�E���݂��Ɍ���������<b>500��$term[2]</b>������܂��B<br>
�E��������͐T�d�ɑI�тȂ����B���̐l�Ə��������Ă����邩�悭�l����̂ł��B<br>
�E���O�ɂ悭�b�������Ȃ����B�Ƃ���v���|�[�Y�����Ă�����͍���ł��傤�B<br>
�E�v���|�[�Y�����������v�ƂȂ�C�󂯂������ȂɂȂ�܂��B
$TRE$TBE<br>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="new">
<BIG>���v���|�[�Y</BIG>�F�� $DT->{name} ($DT->{shopname})��
<SELECT NAME=tg>$userselect</SELECT>
���ȂƂ�<br>
���₩�Ȃ鎞���a�߂鎞�����̐g�����ɂ��鎖��
<INPUT TYPE=SUBMIT VALUE='�����܂�'>
</FORM>
STR
}

sub ConstForm
{
$disp.=<<STR;
$TB$TR$TD
$image[3]
�_���F�Z������Ă�̂ł����H ����Ȃ玟�̒��ӂ��悭�����Ă��������B<br>
�E������<b>1500��$term[2]</b>������܂��B���p�q�ɂ���x�o����܂��B<br>
�E��x���Ă���ꏊ���ڂ邱�Ƃ͂ł��܂���B<br>
$TRE$TBE
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="con">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$Q{idx}">
<INPUT TYPE=HIDDEN NAME=place VALUE="$Q{form}">
<BIG>���Z��z</BIG>�F�w��̏ꏊ�ɏZ���
<INPUT TYPE=SUBMIT VALUE='���z����'>
</FORM>
STR
}
