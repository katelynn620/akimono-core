# �h���S�����[�X �h���S���ڍו\�� 2005/03/30 �R��

$disp.="<BIG>���h���S�����[�X�F�q��</BIG><br><br>";

ReadDragon();
my $cnt=$id2dra{$Q{dr}};
OutError("bad request") if ($DR[$cnt]->{town} ne $MYDIR || $DR[$cnt]->{owner} != $DT->{id});
my $stname="";
$forment="";

ReadStable();
if (scalar @ST)
	{
	foreach(0..$STcount)
		{
		$stname=$ST[$_]->{name} if ($ST[$_]->{no}==$DR[$cnt]->{stable});
		$forment.="<OPTION VALUE=\"$ST[$_]->{no}\">$ST[$_]->{name}";
		}
	}

$disp.="$TB$TR$TDB����$TDB�N��$TDB����$TDB�ѐF$TDB�a���X��$TDB�r��$TDB�����K��$TDB���܋�$TDB����$TDB�o��$TRE";
$disp.=$TR;
$disp.=$TD."<b>".GetTagImgDra($DR[$cnt]->{fm},$DR[$cnt]->{color}).$DR[$cnt]->{name}."</b>";
$disp.=$TD.GetTime2found($NOW_TIME-$DR[$cnt]->{birth});
$disp.=$TD.$FM[$DR[$cnt]->{fm}];
$disp.=$TD.$DRCOLOR[$DR[$cnt]->{color}];
$disp.=$TD.$stname;
$disp.=$TD.$STRATE[ GetRaceStrate($DR[$cnt]->{sr},$DR[$cnt]->{ag}) ];
$disp.=$TD.GetRaceApt($DR[$cnt]->{apt},$DR[$cnt]->{fl})."km";
$disp.=$TD.($DR[$cnt]->{prize} + 0)."��";
$disp.=$TD.($DR[$cnt]->{g1win} + 0)." - ".($DR[$cnt]->{g2win} + 0)." - ".($DR[$cnt]->{g3win} + 0)." - ".($DR[$cnt]->{sdwin} + 0);
$disp.=$TD.$ONRACE[$DR[$cnt]->{race}];
$disp.=$TRE;
$disp.=$TBE."<br>";
$disp.="<BIG>���\\�͂̏ڍ�</BIG><br><br>";
$disp.=$TB;
$disp.=$TR.$TDB."�X�s�[�h".$TD.GetDragonBar($DR[$cnt]->{sp},$DR[$cnt]->{spp}).$TRE;
$disp.=$TR.$TDB."��������".$TD.GetDragonBar($DR[$cnt]->{sr},$DR[$cnt]->{srp}).$TRE;
$disp.=$TR.$TDB."�u����".$TD.GetDragonBar($DR[$cnt]->{ag},$DR[$cnt]->{agp}).$TRE;
$disp.=$TR.$TDB."�p���[".$TD.GetDragonBar($DR[$cnt]->{pw},$DR[$cnt]->{pwp}).$TRE;
$disp.=$TR.$TDB."���N".$TD.GetDragonBar($DR[$cnt]->{hl},$DR[$cnt]->{hlp}).$TRE;
$disp.=$TR.$TDB."�_�".$TD.GetDragonBar($DR[$cnt]->{fl},$DR[$cnt]->{flp}).$TRE;
$disp.=$TR.$TDB."�̒�".$TD.GetConBar($DR[$cnt]->{con}).$TRE;
$disp.=$TR.$TDB."�̏d".$TD.GetWtBar($DR[$cnt]->{wt}).$TRE;
$disp.=$TR.$TDB."�����x".$TD.GetConBar($DR[$cnt]->{gr},1).$TRE;
$disp.=$TBE."<br>";
if ($DR[$cnt]->{race} < 2)
	{
	FormEnt() if (scalar @ST);
	FormToRace();
	FormRetire() if ($NOW_TIME-$DR[$cnt]->{birth} > $DRretire);
	}
1;

sub GetDragonBar
{
	my($point,$up)=@_;
	my $per=$point - $up;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/b.gif" width="|.($per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/r.gif" width="|.($up).qq|" height="12">| if $up;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$point).qq|" height="12">| if $point!=100;
	$bar.=" ".($per + 0)." + ".($up + 0);
	$bar.="</nobr>";
	return $bar;
}

sub GetConBar
{
	my($per,$mode)=@_;
	
	$per=100 if $per > 100;
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/r.gif" width="|.($per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=100;
	$bar.=" ".$EVALUE[int($per/100*4)] if !$mode;
	$bar.=" ".($per + 0)."%";
	$bar.="</nobr>";
	return $bar;
}

sub GetWtBar
{
	my($point)=@_;
	my $per=($point - 40) * 5;
	my $rank=int(($point - 50) / 2);
	$rank=-$rank if ($rank < 0);
	$rank=3 - $rank;
	$rank=0 if $rank < 0;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/r.gif" width="|.($per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=100;
	$bar.=" ".$EVALUE[int($rank)]." ".$point."�g��";
	$bar.="</nobr>";
	return $bar;
}

sub FormEnt
{
my $costmsg=GetMoneyString($STcost);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="dredit">
<INPUT TYPE=HIDDEN NAME=code VALUE="ent">
<INPUT TYPE=HIDDEN NAME=dr VALUE="$Q{dr}">
<BIG>���X�ɗa��</BIG>�F <SELECT NAME=ent SIZE=1>
$forment
</SELECT> �Ƀh���S����
<INPUT TYPE=SUBMIT VALUE='�a��'>
</FORM>
<br>
$TB$TR$TD
�E�X�ɂɃh���S����a������ƁC�����ɂ�鐬���������߂܂��B<br>
�E�a����������<b>$costmsg</b>������܂��B
$TBE<br>
STR
}

sub FormToRace
{
my $formrace="";
my $formjock="<OPTION VALUE=\"0\">�|�|�R��Ȃ��|�|";
my $formstrate="";
foreach (0..$#RACETERM)
	{
	$formrace.="<OPTION VALUE=\"$_\">$RACETERM[$_]";
	}
foreach (0..3)
	{
	$formstrate.="<OPTION VALUE=\"$_\">$STRATE[$_]";
	}
ReadJock();
if (scalar @JK)
	{
	foreach(0..$JKcount)
		{
		next if $JK[$_]->{race} > 1;
		$formjock.="<OPTION VALUE=\"$JK[$_]->{no}\">$JK[$_]->{name}";
		}
	}


$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="dredit">
<INPUT TYPE=HIDDEN NAME=code VALUE="torace">
<INPUT TYPE=HIDDEN NAME=dr VALUE="$Q{dr}">
<BIG>�����[�X�o���o�^</BIG>�F �h���S���� <SELECT NAME=rcode SIZE=1>
$formrace
</SELECT> �ɁC�Ə� <SELECT NAME=jock SIZE=1>
$formjock
</SELECT> ��� <SELECT NAME=str SIZE=1>
$formstrate
</SELECT> �� 
<INPUT TYPE=SUBMIT VALUE='�o��'>
</FORM>
<br>
$TB$TR$TD
�E����𒴂��Ă���ƁC���I�ɂ���ďo���ł��Ȃ��ꍇ������܂��B<br>
�E�o������ƁC���̊Ԃ̒������s���Ȃ������C�̒��E�̏d���������܂��B<br>
�E���[�X�̋�����n���f�C���̏o�ꗳ�Ȃǂ����āC�s���ɂȂ�Ȃ����m�F���܂��傤�B
$TBE<br>
STR
}

sub FormRetire
{
my $remsg=GetTime2found($DRretire);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="predit">
<INPUT TYPE=HIDDEN NAME=code VALUE="retire">
<INPUT TYPE=HIDDEN NAME=dr VALUE="$Q{dr}">
<BIG>������</BIG>�F �h���S����
<INPUT TYPE=SUBMIT VALUE='���ނ�����'>
<INPUT TYPE=TEXT NAME=check SIZE=10 VALUE="">
(retire�Ɠ���) 
</FORM>
<br>
$TB$TR$TD
�E�N�� <b>$remsg</b>�ȏ�̃h���S���́C���ނ����邱�Ƃ��ł��܂��B<br>
�E���܋��� <b>$PRentry��</b>�ȏ�̃h���S���́C��E�ɐB���肵�܂��B
$TBE
STR
}

