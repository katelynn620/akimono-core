# �h���S�����[�X ���[�X�\�� 2005/03/30 �R��

my $rcode=$Q{code};
$rcode||=0;
ReadRace($rcode);
my @MYRACE=@{$RACE[$rcode]};
my @R=@{$MYRACE[$RDS[1]]};
undef @RACE;
undef @MYRACE;	#�s�K�v�Ȕz��͉��

$disp.="<BIG>���h���S�����[�X�F".$RACETERM[$rcode]."</BIG><br><br>";
$disp.="$TB$TR$TD".GetTagImgKao("���[�X��t","slime2").$TD;
$disp.="<SPAN>���[�X��t</SPAN>�F";

if ($RDS[0]>1) {
$disp.="�������܃��[�X���s���Ă��܂��B<br>";
$disp.="���̎��������� ".GetTime2FormatTime($DRTIME[$rcode + 1])." �ł��B";
	}
elsif ($RDS[0]==1) {
$disp.="�o���h���S���͈ȉ��̂Ƃ��茈�肢�����܂����B<br>";
$disp.="���[�X�J�n������ ".GetTime2FormatTime($DRTIME[$rcode + 1])." �ł��B";
	}
else {
$disp.="�������܏o���o�^����t���ł��B<br>";
$disp.="�o�^���ߐ؂�� ".GetTime2FormatTime($DRTIME[$rcode + 1])." �ł��B";
	}

$disp.=$TRE.$TBE."<br>";
$disp.="<b>".$R[0]."</b> (".$RACERANK[$R[1]].") ".$FIELDTYPE[$R[3]].$R[5]."km";
$disp.='<IMG class="i" SRC="'.$IMAGE_URL.'/dragonw'.($RDS[2] + 1).$IMAGE_EXT.'"> ';
$disp.="��� ".$R[9]." �n���f";
$disp.=($R[2] ? "$R[2]����" : "�Ȃ�");
$disp.=qq|<br><IMG class="i" SRC="$IMAGE_URL/guildprize$IMAGE_EXT">|;
$disp.="�܋� ".$R[6]."�� - ".$R[7]."�� - ".$R[8]."��";
$disp.=qq| <input type="button" value="�o�����ڍ�" onclick="javascript:window.open('action.cgi?key=slime-l&mode=rd&rcode=$rcode','_blank','width=760,height=580,scrollbars')">|;
$disp.="<br><br>$TB$TR$TDB�g��$TDB���O$TDB�N��$TDB����$TDB�n���f$TDB�q��$TDB�X��$TDB�R��$TDB���܋�$TDB�r��$TDB�l�C$TDB�ʉ߃^�C��$TRE";

foreach (0..$#RD)
	{
	next if !$RD[$_]->{name};
	$disp.=$TR;
	$disp.=$TD.$RD[$_]->{no};
	$disp.=$TD.GetTagImgDra($RD[$_]->{fm},$RD[$_]->{color}).$RD[$_]->{name};
	$disp.=$TD.GetTime2found($NOW_TIME-$RD[$_]->{birth});
	$disp.=$TD.$FM[$RD[$_]->{fm}];
	$disp.=$TD.($R[2] ? int($RD[$_]->{prize} / $R[2]) : "0");
	$disp.=$TD.$RD[$_]->{rcname};
	$disp.=$TD.$RD[$_]->{stname};
	$disp.=$TD.$RD[$_]->{jkname};
	$disp.=$TD.($RD[$_]->{prize} + 0)."��";
	$disp.=$TD.$STRATE[ $RD[$_]->{strate} ];
	$disp.=$TD.$RD[$_]->{pop};
	$disp.=$TD.GetRaceTime($RD[$_]->{time});
	$disp.=$TRE;
	}
$disp.=$TBE."<br>";

ReadRaceLog($rcode);
$disp.=$TB.$TR.$TD.GetTagImgKao("���[�X��t","slime6","align=left ")."<SPAN>�����A�i�E���T�[</SPAN><br>".$RACELOG.$TRE.$TBE if ($RACELOG);
1;

sub ReadRaceLog
{
	my($f)=@_;
	$f||=0;
	my $fn=GetPath($COMMON_DIR,"dra-rlog$f");
	undef $RACELOG;
	open(IN,$fn) or return;
	read(IN,$RACELOG,-s $fn);
	close(IN);
}

