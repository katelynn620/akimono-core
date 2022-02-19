# �h���S�����[�X �h���S�������e 2005/03/30 �R��

ReadDragon();
$disp.="<BIG>���h���S�����[�X�F�q��</BIG><br><br>";

my $functionname=$Q{code};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteDragon();
CoDataCA();
1;

sub retire
{
	#�h���S���`�F�b�N
	my $cnt=$id2dra{$Q{dr}};
	OutError("bad request") if ($DR[$cnt]->{town} ne $MYDIR || $DR[$cnt]->{owner} != $DT->{id});
	OutError("bad request") if ($DR[$cnt]->{race} > 1);
	OutError("bad request") if ($NOW_TIME-$DR[$cnt]->{birth} < $DRretire);

	OutError("�h���S�������ނ�����ɂ� retire �Ɠ��͂��Ă�������") if ($Q{check} ne "retire");

	$disp.="�h���S���u".$DR[$cnt]->{name}."�v�����ނ����܂����B";

	if ($DR[$cnt]->{prize} >= $PRentry)
	{
	$disp.="<br>��������̊���ɂ��C".($DR[$cnt]->{fm} ? "�ɐB" : "��").$FM[$DR[$cnt]->{fm}]."�����肪�F�߂��܂����B";
	PushDraLog(0,"�h���S���u".$DR[$cnt]->{name}."�v�����ނ��C".($DR[$cnt]->{fm} ? "�ɐB" : "��").$FM[$DR[$cnt]->{fm}]."�����肵�܂����B");
	RenewDraLog();

	ReadParent();
	
	@PR=reverse(@PR);
	$PRcount++;
	my $i=$PRcount;
	$PR[$i]->{no}=($i > 0) ? ($PR[$i-1]->{no} + 1) : 1 ;
	$PR[$i]->{birth}=$DR[$cnt]->{birth};
	$PR[$i]->{fm}=$DR[$cnt]->{fm};
	$PR[$i]->{color}=$DR[$cnt]->{color};
	$PR[$i]->{name}=$DR[$cnt]->{name};
	$PR[$i]->{town}=$MYDIR;
	$PR[$i]->{owner}=$DT->{id};
	$PR[$i]->{apt}=$DR[$cnt]->{apt};
	$PR[$i]->{hr}=int(rand(95)) + 5;

	$PR[$i]->{sp}=$DR[$cnt]->{sp} - $DR[$cnt]->{spp};
	$PR[$i]->{sr}=$DR[$cnt]->{sr} - $DR[$cnt]->{srp};
	$PR[$i]->{ag}=$DR[$cnt]->{ag} - $DR[$cnt]->{agp};
	$PR[$i]->{pw}=$DR[$cnt]->{pw} - $DR[$cnt]->{pwp};
	$PR[$i]->{hl}=$DR[$cnt]->{hl} - $DR[$cnt]->{hlp};
	$PR[$i]->{fl}=$DR[$cnt]->{fl} - $DR[$cnt]->{flp};

	$PR[$i]->{prize}=$DR[$cnt]->{prize};
	$PR[$i]->{sdwin}=$DR[$cnt]->{sdwin};
	$PR[$i]->{g3win}=$DR[$cnt]->{g3win};
	$PR[$i]->{g2win}=$DR[$cnt]->{g2win};
	$PR[$i]->{g1win}=$DR[$cnt]->{g1win};

	@PR=reverse(@PR);
	WriteParent();
	}

	undef $DR[$cnt];
}


sub preg
{
	OutError('����ȏ�h���S�������L�ł��܂���B') if (scalar @MYDR >= $MYDRmax);

	ReadParent();

	#���h���S���`�F�b�N
	my $p=$id2pr{$Q{dr}};
	OutError("bad request") if ($MYDIR ne $PR[$p]->{town});
	OutError("bad request") if ($PR[$p]->{owner}!=$DT->{id});
	OutError("bad request") if (!$PR[$p]->{fm});
	OutError("bad request") if ($NOW_TIME-$PR[$p]->{preg} < $PRcycle);

	#��h���S���`�F�b�N
	my $q=$id2pr{$Q{pr}};
	OutError("bad request") if ($PR[$q]->{fm});

	# ���O�̐��������`�F�b�N
	require $JCODE_FILE;
	if(!$Q{name})
	{
		OutError('���O����͂��Ă��������B');
	}
	$Q{name}=jcode::sjis($Q{name},$CHAR_SHIFT_JIS&&'sjis');
	if($Q{name} =~ /([,:;\t\r\n<>&])/ || CheckNGName($Q{name}) )
	{
		OutError('���O�Ɏg�p�ł��Ȃ��������܂܂�Ă��܂��B');
	}

	#��xEUC�ɕϊ�
	&jcode::convert(\$Q{name}, "euc", "sjis");
	$ZkatakanaExt = '(?:\xA5[\xA1-\xF6]|\xA1[\xA6\xBC\xB3\xB4])';
	OutError('���O�͑S�p�J�^�J�i�Ŏw�肵�Ă��������B') if ($Q{name} !~ /^($ZkatakanaExt)*$/);
	&jcode::convert(\$Q{name}, "sjis", "euc");

	OutError('���O���������܂��B') if length($Q{name})>20;
	OutError('���O���Z�����܂��B') if length($Q{name})<6;

	@DR=reverse(@DR);
	$DRcount++;
	my $i=$DRcount;
	$DR[$i]->{no}=($i > 0) ? ($DR[$i-1]->{no} + 1) : 1 ;
	$DR[$i]->{birth}=$NOW_TIME;
	$DR[$i]->{fm}=int(rand(2));
	$DR[$i]->{color}=int(rand(scalar @DRCOLOR));
	$DR[$i]->{name}=$Q{name};
	$DR[$i]->{town}=$MYDIR;
	$DR[$i]->{owner}=$DT->{id};

	my @preg=qw(
		apt sp sr ag pw hl fl
		);

	foreach(0..$#preg)
		{
		my $m=$preg[$_];
		$DR[$i]->{$m}=int(($PR[$p]->{$m} * $PR[$p]->{hr} + $PR[$q]->{$m} * $PR[$q]->{hr}) / ($PR[$p]->{hr} + $PR[$q]->{hr}));
		next if !$_;
		$DR[$i]->{$m}=int(($DR[$i]->{$m} * 4 + rand($DR[$i]->{$m}) * 2) / 5);
		$DR[$i]->{$m}=100 if ($DR[$i]->{$m} > 100);
		}

	$DR[$i]->{apt}=int(($DR[$i]->{apt} * 100 + 50) / 100);
	$DR[$i]->{con}=30 + int(rand(10));
	$DR[$i]->{wt}=43 + int(rand(3));

	@DR=reverse(@DR);

	$PR[$p]->{preg}=$NOW_TIME;
	WriteParent();

$disp.="�V�����h���S���u<b>".$Q{name}."</b>�v���a�����܂����B";
}

