# �h���S�����[�X �q�ꃁ�j���[�\�� 2005/03/30 �R��

ReadRanch();
$disp.="<BIG>���h���S�����[�X�F�q��</BIG><br><br>";

if ($MYRC==-1)
{
$disp.="$TB$TR$TD".GetTagImgKao("�h���S���V�t","slime1").$TD;
$disp.="<SPAN>�h���S���V�t</SPAN>�F�����̖q��������Ă��Ȃ��悤����ȁB<br>";
$disp.="�q������Ă΁C�����̃h���S������Ă邱�Ƃ��ł���B".$TRE.$TBE;
my $estmsg=GetMoneyString($RCest);
$disp.=<<STR;
<br>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="rcedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>���q��ݗ�</BIG>�F <INPUT TYPE=TEXT NAME=name SIZE=20> �Ɩ��t���� 
<INPUT TYPE=SUBMIT VALUE='�ݗ�'>
</FORM>
<br>
$TB$TR$TD
�E�q���ݗ�����ɂ́C����<b>$estmsg</b>��������܂��B<br>
�E�h���S���̈琬�ɂ͕ʓr����Ɏ�����������̂ŁC�]�T�����邩�l���Ă��������B<br>
$TBE
STR
}
else
{
$disp.="$TB$TR$TDB����$TDB�n��$TDB���Ϗ܋�$TDB���܋�$TDB����$TRE";
$disp.=$TR;
$disp.=$TD.$RC[$MYRC]->{name};
$disp.=$TD.GetTime2found($NOW_TIME-$RC[$MYRC]->{birth});
$disp.=$TD.($RC[$MYRC]->{aprize} + 0)."��";
$disp.=$TD.($RC[$MYRC]->{prize} + 0)."��";
$disp.=$TD.($RC[$MYRC]->{g1win} + 0)." - ".($RC[$MYRC]->{g2win} + 0)." - ".($RC[$MYRC]->{g3win} + 0)." - ".($RC[$MYRC]->{sdwin} + 0);
$disp.=$TRE.$TBE;
$disp.="<br><BIG>�����L������</BIG><br><br>";
ReadDragon();
if (!scalar @MYDR)
	{
	$disp.="���L�̋������͂���܂���<br><br>";
	}
	else
	{
$disp.="$TB$TR$TDB����$TDB�N��$TDB����$TDB�X�s$TDB����$TDB�u��$TDB�p��$TDB�̒�$TDB�̏d$TDB�����K��$TDB���܋�$TDB����$TRE";
	foreach (@MYDR)
		{
$disp.=$TR;
$disp.=$TD."<a href=\"action.cgi?key=slime&mode=detail&dr=$DR[$_]->{no}&$USERPASSURL\">"
	.GetTagImgDra($DR[$_]->{fm},$DR[$_]->{color}).$DR[$_]->{name}."</a>";
$disp.=$TD.GetTime2found($NOW_TIME-$DR[$_]->{birth});
$disp.=$TD.$FM[$DR[$_]->{fm}];
$disp.=$TD.$VALUE[int($DR[$_]->{sp} /100*6)];
$disp.=$TD.$VALUE[int($DR[$_]->{sr} /100*6)];
$disp.=$TD.$VALUE[int($DR[$_]->{ag} /100*6)];
$disp.=$TD.$VALUE[int($DR[$_]->{pw} /100*6)];
$disp.=$TD.$EVALUE[int($DR[$_]->{con} /100*4)];
$disp.=$TD.$DR[$_]->{wt};
$disp.=$TD.GetRaceApt($DR[$_]->{apt},$DR[$_]->{fl});
$disp.=$TD.($DR[$_]->{prize} + 0)."��";
$disp.=$TD.($DR[$_]->{g1win} + 0)." - ".($DR[$_]->{g2win} + 0)." - ".($DR[$_]->{g3win} + 0)." - ".($DR[$_]->{sdwin} + 0);
$disp.=$TRE;
		}
$disp.=$TBE."<br>";
	}

ReadParent();

if (scalar @MYPR)
	{
	$disp.="<BIG>�����L�ɐB".$FM[1]."��</BIG><br><br>";
$disp.="$TB$TR$TDB����$TDB�N��$TDB��`$TDB�X�s$TDB����$TDB�u��$TDB�p��$TDB���N$TDB�_��$TDB�����K��$TDB�����܋�$TDB���𐬐�$TRE";
	foreach (@MYPR)
		{
$disp.=$TR;
$disp.=$TD."<a href=\"action.cgi?key=slime&mode=pr&dr=$PR[$_]->{no}&$USERPASSURL\">"
	.GetTagImgDra($PR[$_]->{fm},$PR[$_]->{color},1).$PR[$_]->{name}."</a>";
$disp.=$TD.GetTime2found($NOW_TIME-$PR[$_]->{birth});
$disp.=$TD.$VALUE[int($PR[$_]->{hr} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{sp} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{sr} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{ag} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{pw} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{hl} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{fl} /100*6)];
$disp.=$TD.GetRaceApt($PR[$_]->{apt},$PR[$_]->{fl});
$disp.=$TD.($PR[$_]->{prize} + 0)."��";
$disp.=$TD.($PR[$_]->{g1win} + 0)." - ".($PR[$_]->{g2win} + 0)." - ".($PR[$_]->{g3win} + 0)." - ".($PR[$_]->{sdwin} + 0);
$disp.=$TRE;
		}
$disp.=$TBE."<br>";
	}



if (scalar @MYDR < $MYDRmax)
	{
my @dist=('�Z������','��������','��������');
my $formdist="";
foreach(0..$#dist) {$formdist.=qq|<OPTION VALUE="$_">$dist[$_]|; }
my $buymsg=GetMoneyString($DRbuy);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="dredit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>���h���S���w��</BIG>�F <SELECT NAME=fm SIZE=1>
<OPTION VALUE="0">$FM[0]<OPTION VALUE="1">$FM[1]
</SELECT> �� <SELECT NAME=dist SIZE=1>
$formdist
</SELECT> �� 
<INPUT TYPE=TEXT NAME=name SIZE=20> �Ɩ��t���� 
<INPUT TYPE=SUBMIT VALUE='�w��'>
</FORM>
<br>
$TB$TR$TD
�E�������́C<b>$MYDRmax</b>���܂Ŏ����Ƃ��ł��܂��B<br>
�E�w������ɂ́C����<b>$buymsg</b>��������܂��B<br>
�E���O�́C<b>�S�p�J�^�J�i10����</b>�ȓ��ł��B
$TBE
STR
	}
}
1;



