# �h���S�����[�X �R�胁�j���[�\�� 2005/03/30 �R��

ReadJock();
$disp.="<BIG>���h���S�����[�X�F�R��</BIG><br><br>";

if ($MYJK==-1)
{
$disp.="$TB$TR$TD".GetTagImgKao("�R�蒇��","slime5").$TD;
$disp.="<SPAN>�R�蒇��</SPAN>�F�R����ق��Ă��Ȃ��񂾂ȁB<br>";
$disp.="�R����ق��΁C�����⑼�l�̃h���S���̗͂����[�X�ň����o����B".$TRE.$TBE."<br>";
if (scalar @JK < $JKmax)
	{
	FormJock();
	}
	else
	{
	$disp.="<BIG>���R��ٗp</BIG>�F ����ɒB���Ă��邽�߁C����ȏ�ٗp�ł��܂���B";
	}
}
else
{
$disp.="$TB$TR$TDB���O$TDB�Α�$TDB����$TDB����$TDB����$TDB����\\��$TDB�o��$TRE";
$disp.=$TR;
$disp.=$TD.$JK[$MYJK]->{name};
$disp.=$TD.GetTime2found($NOW_TIME-$JK[$MYJK]->{birth});
$disp.=$TD.$VALUE[int($JK[$MYJK]->{ahead} /100*6)];
$disp.=$TD.$VALUE[int($JK[$MYJK]->{back} /100*6)];
$disp.=$TD.($JK[$MYJK]->{g1win} + 0)." - ".($JK[$MYJK]->{g2win} + 0)." - ".($JK[$MYJK]->{g3win} + 0)." - ".($JK[$MYJK]->{sdwin} + 0);
$disp.=$TD."<small>".$JKSP[($JK[$MYJK]->{sp} + 0)]."</small>";
$disp.=$TD.$ONRACE[$JK[$MYJK]->{race}];
$disp.=$TRE.$TBE;
}
1;

sub FormJock
{
my $estmsg=GetMoneyString($JKest);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="jkedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>���R��ٗp</BIG>�F <INPUT TYPE=TEXT NAME=name SIZE=20> �Ɩ��t���� 
<INPUT TYPE=SUBMIT VALUE='�ٗp'>
</FORM>
<br>
$TB$TR$TD
�E�R����ٗp����ɂ́C����<b>$estmsg</b>��������܂��B<br>
�E�R��͑S�̂� <b>$JKmax</b>�l�̒��������C�����ɂȂ�ƌٗp�ł��܂���B
$TBE
STR
}

