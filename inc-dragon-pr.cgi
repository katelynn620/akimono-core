# �h���S�����[�X �B���h���S���ڍו\�� 2005/03/30 �R��

$disp.="<BIG>���h���S�����[�X�F�q��</BIG><br><br>";

ReadParent();
my $cnt=$id2pr{$Q{dr}};
OutError("bad request") if ($MYDIR ne $PR[$cnt]->{town});
OutError("bad request") if ($PR[$cnt]->{owner}!=$DT->{id});
OutError("bad request") if (!$PR[$cnt]->{fm});

$forment="";
foreach(0..$PRcount)
	{
	next if $PR[$_]->{fm};
	$forment.="<OPTION VALUE=\"$PR[$_]->{no}\">$PR[$_]->{name}";
	}

$disp.="$TB$TR$TDB����$TDB�N��$TDB�ѐF$TDB�r��$TDB�����K��$TDB�����܋�$TDB���𐬐�$TDB�O��̏o�Y$TRE";
$disp.=$TR;
$disp.=$TD."<b>".GetTagImgDra($PR[$cnt]->{fm},$PR[$cnt]->{color},1).$PR[$cnt]->{name}."</b>";
$disp.=$TD.GetTime2found($NOW_TIME-$PR[$cnt]->{birth});
$disp.=$TD.$DRCOLOR[$PR[$cnt]->{color}];
$disp.=$TD.$STRATE[ GetRaceStrate($PR[$cnt]->{sr},$PR[$cnt]->{ag}) ];
$disp.=$TD.GetRaceApt($PR[$cnt]->{apt},$PR[$cnt]->{fl})."km";
$disp.=$TD.($PR[$cnt]->{prize} + 0)."��";
$disp.=$TD.($PR[$cnt]->{g1win} + 0)." - ".($PR[$cnt]->{g2win} + 0)." - ".($PR[$cnt]->{g3win} + 0)." - ".($PR[$cnt]->{sdwin} + 0);
$disp.=$TD.GetTime2FormatTime($PR[$cnt]->{preg});
$disp.=$TRE;
$disp.=$TBE."<br>";
$disp.="<BIG>���\\�͂̏ڍ�</BIG><br><br>";
$disp.=$TB;
$disp.=$TR.$TDB."��`��".$TD.GetParentBar($PR[$cnt]->{hr}).$TRE;
$disp.=$TR.$TDB."�X�s�[�h".$TD.GetParentBar($PR[$cnt]->{sp}).$TRE;
$disp.=$TR.$TDB."��������".$TD.GetParentBar($PR[$cnt]->{sr}).$TRE;
$disp.=$TR.$TDB."�u����".$TD.GetParentBar($PR[$cnt]->{ag}).$TRE;
$disp.=$TR.$TDB."�p���[".$TD.GetParentBar($PR[$cnt]->{pw}).$TRE;
$disp.=$TR.$TDB."���N".$TD.GetParentBar($PR[$cnt]->{hl}).$TRE;
$disp.=$TR.$TDB."�_�".$TD.GetParentBar($PR[$cnt]->{fl}).$TRE;
$disp.=$TBE."<br>";
if ($forment && ($NOW_TIME-$PR[$cnt]->{preg} > $PRcycle))
	{
	FormPreg();
	}
1;

sub GetParentBar
{
	my($per)=@_;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/b.gif" width="|.($per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=100;
	$bar.=" ".($per + 0);
	$bar.="</nobr>";
	return $bar;
}

sub FormPreg
{
my $prmsg=GetTime2found($PRcycle);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="predit">
<INPUT TYPE=HIDDEN NAME=code VALUE="preg">
<INPUT TYPE=HIDDEN NAME=dr VALUE="$Q{dr}">
<BIG>����t��</BIG>�F ���܂��h���S���� 
<INPUT TYPE=TEXT NAME=name SIZE=20> �Ɩ��t���� 
<SELECT NAME=pr SIZE=1>
$forment
</SELECT> �� 
<INPUT TYPE=SUBMIT VALUE='��t������'>
</FORM>
<br>
$TB$TR$TD
�E�����������ł� <b>$MYDRmax</b>������Ƃ��́C��t�������s�ł��܂���B<br>
�E���O�́C<b>�Ђ炪��10����</b>�ȓ��ł��B<br>
�E��$FM[0]���̏��L�҂ɁC��t�������x�����܂��B<br>
�E�o�Y����ƁC<b>$prmsg</b>�Ԃ͎��̎�t�����ł��܂���B
$TBE<br>
STR
}

