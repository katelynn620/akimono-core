# �h���S�����[�X �X�Ƀ��j���[�\�� 2005/03/30 �R��

ReadStable();
$disp.="<BIG>���h���S�����[�X�F�X��</BIG><br><br>";

if ($MYST==-1)
{
$disp.="$TB$TR$TD".GetTagImgKao("�h���S�������t","slime3").$TD;
$disp.="<SPAN>�h���S�������t</SPAN>�F�����̉X�ɂ������Ă��Ȃ��悤���ȁB<br>";
$disp.="�X�ɂ����Ă΁C�����⑼�l�̃h���S���𒲋����邱�Ƃ��ł���B".$TRE.$TBE."<br>";
if (scalar @ST < $STmax)
	{
	FormStable();
	}
	else
	{
	$disp.="<BIG>���X�ɐݗ�</BIG>�F �萔�ɒB���Ă��邽�߁C����ȏ�ݗ��ł��܂���B";
	}
}
else
{
	$disp.="$TB$TR$TDB����$TDB���j$TDB����$TDB�̒�$TDB�̏d$TDB�R�[�X$TDB����$TDB��H$TDB�_�[�g$TDB����$TDB�q�{$TDB����$TDB�ێ���$TDB�V����$TRE";
	$disp.=$TR;
	$disp.=$TD.$ST[$MYST]->{name};
	$disp.=$TD.$EMPHA[$ST[$MYST]->{emp}];
	$disp.=$TD.$VALUE[int($ST[$MYST]->{tr} /100*6)];
	$disp.=$TD.$VALUE[int($ST[$MYST]->{con} /100*6)];
	$disp.=$TD.$VALUE[int($ST[$MYST]->{wt} /100*6)];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{sp}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{sr}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{ag}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{pw}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{hl}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{fl}];
	$disp.=$TD.($ST[$MYST]->{g1win} + 0)." - ".($ST[$MYST]->{g2win} + 0)." - ".($ST[$MYST]->{g3win} + 0)." - ".($ST[$MYST]->{sdwin} + 0);
	$cost=($ST[$MYST]->{sp} + $ST[$MYST]->{sr} + $ST[$MYST]->{ag} + $ST[$MYST]->{pw} + $ST[$MYST]->{hl} + $ST[$MYST]->{fl});
	$disp.=$TD.GetMoneyString($cost * $STcost);
	my $limit=$ST[$MYST]->{birth} + $STtime - $NOW_TIME;
	$disp.=$TD."���� ".(($limit > 0) ? GetTime2found($limit) : "�킸��");
	$disp.=$TRE.$TBE."<br>";
	StableDragon();
	FormLarge();
}
1;

sub FormStable
{
my $estmsg=GetMoneyString($STest);
my $costmsg=GetMoneyString($STcost);
my $formemp;
	foreach (0..$#EMPHA)
	{
	$formemp.="<OPTION VALUE=\"$_\">$EMPHA[$_]";
	}
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="stedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>���X�ɐݗ�</BIG>�F <SELECT NAME=emp SIZE=1>
$formemp
</SELECT> �𒲋����j�Ƃ���X�ɂ� <INPUT TYPE=TEXT NAME=name SIZE=20> �Ɩ��t���� 
<INPUT TYPE=SUBMIT VALUE='�ݗ�'>
</FORM>
<br>
$TB$TR$TD
�E�X�ɂ�ݗ�����ɂ́C����<b>$estmsg</b>��������܂��B<br>
�E�ێ���Œ�ł�����<b>$costmsg</b>������܂��B<br>
�E�������j��I�ׂ܂��B�ォ��ύX���邱�Ƃ͂ł��܂���B<br>
�E�X�ɂ͑S�̂� <b>$STmax</b>�ɂ̏��������C���t�ɂȂ�Ɛݗ��ł��܂���B
$TBE
STR
}

sub StableDragon
{
	$disp.="<BIG>�����X���̗�</BIG><br><br>";
	ReadDragon();
	$disp.="$TB$TR$TDB����$TDB�N��$TDB����$TDB�̒�$TDB�̏d$TDB���܋�$TDB����$TRE";
	foreach(0..$#DR)
	{
	next if ($DR[$_]->{stable} != $ST[$MYST]->{no});
$disp.=$TR;
$disp.=$TD.GetTagImgDra($DR[$_]->{fm},$DR[$_]->{color}).$DR[$_]->{name};
$disp.=$TD.GetTime2found($NOW_TIME-$DR[$_]->{birth});
$disp.=$TD.$FM[$DR[$_]->{fm}];
$disp.=$TD.$EVALUE[int($DR[$_]->{con} /100*4)];
$disp.=$TD.$DR[$_]->{wt};
$disp.=$TD.($DR[$_]->{prize} + 0)."��";
$disp.=$TD.($DR[$_]->{g1win} + 0)." - ".($DR[$_]->{g2win} + 0)." - ".($DR[$_]->{g3win} + 0)." - ".($DR[$_]->{sdwin} + 0);
$disp.=$TRE;
	}
$disp.=$TBE."<br>";
}


sub FormLarge
{
my $n=int(($NOW_TIME - $ST[$MYST]->{birth})/86400/2) + 1;
if ($n < $cost)
	{
	$disp.="<BIG>���X�ɑ��z</BIG>�F �܂�����ȏ�̑��z�͂ł��܂���";
	return;
	}
my $estmsg=GetMoneyString($STest);
my @LARGE=(
	'�g���b�N�R�[�X (�X�s�[�h�㏸)',
	'������ (���������㏸)',
	'��H�{�� (�u���͏㏸)',
	'�_�[�g�g���b�N (�p���[�㏸)',
	'����{�� (���N�㏸)',
	'�q�{�{�� (�_��㏸)'
);
my $formemp;
	foreach (0..$#LARGE)
	{
	$formemp.="<OPTION VALUE=\"$_\">$LARGE[$_]";
	}
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="stedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="large">
<BIG>���X�ɑ��z</BIG>�F <SELECT NAME=lar SIZE=1>
$formemp
</SELECT> �� <INPUT TYPE=SUBMIT VALUE='���z'>
</FORM>
<br>
$TB$TR$TD
�E�X�ɂ𑝒z����ɂ́C����<b>$estmsg</b>��������܂��B<br>
�E���z����ƈێ������������悤�ɂȂ�܂��B<br>
�E�a�����̎������ێ������ƁC�Ԏ��ɂȂ�̂ł����ӂ��������B
$TBE
STR
}

