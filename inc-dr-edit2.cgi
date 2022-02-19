# �h���S�����[�X ���[�X�W�J 2005/03/30 �R��

if ($NOW_TIME > $DRTIME[2]) { $rcode=1; } else { $rcode=0; }

ReadRace($rcode);

@MYRACE=@{$RACE[$rcode]};
@R=@{$MYRACE[$RDS[1]]};
undef $RACELOG;
if (!$RDS[0])
	{
	Entry();
	}
	else
	{
	my $functionname="Race".$RDS[0];
	&$functionname;
	}
WriteRaceLog($rcode,$RACELOG) if $RACELOG;
WriteRace($rcode);
WriteDrLast();
RenewDraLog();
CoDataCA();
CoUnLock();
1;


sub WriteRaceLog
{
	my($f,$message)=@_;
	$f||=0;
	my $fn=GetPath($COMMON_DIR,"dra-rlog$f");
	open(OUT,">>$fn") or return;
	print OUT $message;
	close(OUT);
}

sub Entry
{
	# �o���X���C���m�菈��
	ReadDragon();
	ReadJock();

	if (scalar @RD < 3)
		{
		# �o�������R�ɖ����Ȃ��ꍇ�͑S�����I��������
		foreach(0..$#RD)
			{
			my $id=$RD[$_]->{dr};
			$DR[$id2dra{$id}]->{race}=1 if (defined $id2dra{$id});

			$id=$RD[$_]->{jock};
			$JK[$id2jk{$id}]->{race}=1 if (defined $id2jk{$id});

			undef $RD[$_];

			}
		PushDraLog($rcode+1,$R[0]."�͏o�����s���̂��ߊJ�Â��������܂����B");
		$DRTIME[$rcode+1]+=86400*2;
		$RDS[1]++;
		$RDS[1]=0 if ($RDS[1] > $#MYRACE);
		$RDS[2]=int(rand(2));
		}
		else
		{
		PushDraLog($rcode+1,$R[0]."�̏o���o�^�����ߐ؂��܂����B");
		# �o����������𒴂���ꍇ�͒��I
		if (scalar @RD > $R[9])
			{
			foreach(0..$#RD) { $RD[$_]->{rnd}=($RD[$_]->{prize} * 10000) + int(rand(10000));}
			if ($rcode)
				{
				@RD=sort{$b->{rnd}<=>$a->{rnd}}@RD;	#�d�܃��[�X�͑傫����
				}
				else
				{
				@RD=sort{$a->{rnd}<=>$b->{rnd}}@RD;	#�o�����[�X�͏�������
				}
			foreach($R[9]..$#RD)
				{
				#���I
				my $id=$RD[$_]->{dr};
				$DR[$id2dra{$id}]->{race}=1 if (defined $id2dra{$id});

				$id=$RD[$_]->{jock};
				$JK[$id2jk{$id}]->{race}=1 if (defined $id2jk{$id});
				undef $RD[$_];
				}
			PushDraLog($rcode+1,"�o���������̂��߁C���I���s���܂����B");
			}

		#�o������
		my $num=$R[9] - 1;
		foreach(0..$num)
			{
			next if !$RD[$_]->{name};
			$RD[$_]->{no}=$_ + 1;	#�g�ԐU�蒼��
			my $id=$RD[$_]->{dr};
			$DR[$id2dra{$id}]->{race}=3 if (defined $id2dra{$id});

			$id=$RD[$_]->{jock};
			$JK[$id2jk{$id}]->{race}=3 if (defined $id2jk{$id});
			}

		$DRTIME[$rcode+1]+=3600*2;
		$RDS[0]++;
		}
	my $fn=GetPath($COMMON_DIR,"dra-rlog$rcode");
	unlink $fn if -e $fn;				#�ߋ��̎������O����
	WriteDragon();
	WriteJock();
}

sub Race1
{
	# �l�C�̌���
	foreach(0..$#RD) { $RD[$_]->{sumsp}=$RD[$_]->{prize}*100 + int(rand(100)); }
	@RD=sort{$b->{sumsp}<=>$a->{sumsp}}@RD;

	foreach(0..$#RD)
		{
		$RD[$_]->{pop}=$_ + 1;		#�l�C���o��
		$RD[$_]->{time}+=int($R[5] * 1000 / 4 / $RD[$_]->{sp1});
		}
	@RD=sort{$a->{time}<=>$b->{time}}@RD;

	$RACELOG.="����ł� <b>".$R[0]."</b>�̏o���ł�<br>\n";
	$RACELOG.="���X�����������������낢<br>\n" if $R[1]==5;
	$RACELOG.="�h������ɂ���̂� �ʂ����Ăǂ̗��Ȃ̂�<br>\n" if $R[1]==0;
	$RACELOG.="���̃R�[�X�̏I�Ղ͍�ɂȂ��Ă��܂� ��g�����邩������܂���<br>\n" if $R[4];
	$RACELOG.="���� �X�^�[�g�ł�<br>\n";

	if ($RD[0]->{strate}< 2)
		{
		$RACELOG.="�g�b�v�ɗ������̂� <b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b><br>\n";
		$RACELOG.="����̗\\�z�ʂ�Ƃ������Ƃ���ł��傤��<br>\n";
		}
		else
		{
		$RACELOG.="�Ȃ�� <b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b> �������Ȃ�g�b�v�ɗ����܂���<br>\n";
		$RACELOG.="����� ���Ȃ̂�<br>\n";
		}

	#�C�ӂ̂P�����Љ�
	my $i=int(rand($#RD))+1;
	$RACELOG.="���� ".($i + 1)."�Ԗڂ𑖂��Ă���̂� ".$RD[$i]->{no}."�g <b>".GetTagImgDra($RD[$i]->{fm},$RD[$i]->{color}).$RD[$i]->{name}."</b><br>\n";
	if ($RD[$i]->{pop} < 4)
		{
		$RACELOG.=$RD[$i]->{pop}."�Ԑl�C�̊��҂��� ���̈ʒu���珟����_���܂�<br>\n";
		}
		else
		{
		$RACELOG.="�l�C�� ".$RD[$i]->{pop}."�ԂƂȂ�܂����� �ʂ����Ă��̗��͕����ƂȂ�ł��傤��<br>\n";
		}

	$DRTIME[$rcode+1]+=3600*8;
	$RDS[0]++;
}

sub Race2
{
	my $no=$RD[0]->{no};	#�ȑO�̂P�ʂ��T���Ă���
	foreach(0..$#RD)
		{
		$RD[$_]->{time}+=int($R[5] * 1000 / 4 / $RD[$_]->{sp2});
		}
	@RD=sort{$a->{time}<=>$b->{time}}@RD;

	$RACELOG.="�ŏ��̃R�[�i�[�����܂���<br>\n";
	if ($no == $RD[0]->{no})
		{
		$RACELOG.="���� �g�b�v�͕ς�炸 <b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b><br>\n";
		$RACELOG.="���̐����� �Ō�܂ő����̂�<br>\n";
		}
		else
		{
		$RACELOG.="������ �g�b�v���ς�� ";
		$RACELOG.="�g�b�v�� <b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b><br>\n";
		}

	#���[�X�W�J���� ������
	$RACELOG.="����".($R[5] / 2)."km�̒ʉ߃^�C���� ".GetRaceTime($RD[0]->{time})."<br>\n";
	$RACELOG.="�ق� ����ǂ���Ƃ�����ł��傤 �W�J�ɂ��قǉe���͂Ȃ������ł�<br>\n";

	#�����n�̂P�����Љ�
	my $i=int(rand($#RD))+1;
	foreach(1..$#RD)
		{
		$i=$_,last if ($RD[$_]->{strate}==2 || $RD[$_]->{strate}==3);
		}
	$RACELOG.="<b>".GetTagImgDra($RD[$i]->{fm},$RD[$i]->{color}).$RD[$i]->{name}."</b> �����ʒu�� �������� �g�b�v��_���̂�<br>\n";

	$DRTIME[$rcode+1]+=3600*8;
	$RDS[0]++;
}

sub Race3
{
	my $no=$RD[0]->{no};
	foreach(0..$#RD)
		{
		$RD[$_]->{time}+=int($R[5] * 1000 / 4 / $RD[$_]->{sp3});
		}
	@RD=sort{$a->{time}<=>$b->{time}}@RD;

	$RACELOG.="�㑱���������l�߂Ă����܂�<br>\n";
	if ($no == $RD[0]->{no})
		{
		$RACELOG.="���� �ǂ���</b> ";
		$RACELOG.="�g�b�v�͕ς�炸 <b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b><br>\n";
		$RACELOG.="���̂܂� �����؂��̂� ";
		}
		else
		{
		$RACELOG.="<b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b> ���������I<br>\n";
		$RACELOG.="���� �ǂ���</b> ";
		}
	$RACELOG.="���ǂ��̂� <b>".GetTagImgDra($RD[1]->{fm},$RD[1]->{color}).$RD[1]->{name}."</b><br>\n";

	#�����n�̂P�����Љ�
	my $i=int(rand($#RD))+1;
	foreach(2..$#RD)
		{
		$i=$_,last if ($RD[$_]->{strate}==2 || $RD[$_]->{strate}==3);
		}
	$RACELOG.="<b>".GetTagImgDra($RD[$i]->{fm},$RD[$i]->{color}).$RD[$i]->{name}."</b> ��������肾�� �ǂ���<br>\n";

	$DRTIME[$rcode+1]+=3600*6;
	$RDS[0]++;
}

sub Race4
{
	my $no=$RD[0]->{no};
	foreach(0..$#RD)
		{
		$RD[$_]->{time}+=int($R[5] * 1000 / 4 / $RD[$_]->{sp4});
		}
	@RD=sort{$a->{time}<=>$b->{time}}@RD;

	my $name1=GetTagImgDra($RD[0]->{fm},$RD[0]->{color})."<b>".$RD[0]->{name}."</b>";
	my $name2=GetTagImgDra($RD[1]->{fm},$RD[1]->{color})."<b>".$RD[1]->{name}."</b>";

	$RACELOG.="�Ō�̃R�[�i�[���܂���� �����ɓ���܂�<br>\n";
	if ($no == $RD[0]->{no})
			{
			# �g�b�v�ς�炸
			$RACELOG.="���� �ǂ��� ";
			$RACELOG.="$name2 ���ǂ��グ��<br>\n";
			$RACELOG.="$name1 �������� ���̂܂ܓ����؂邩<br>\n";

			if ($RD[1]->{time} - $RD[0]->{time} < 15)
				{
				$RACELOG.="$name2 ������I ������ $name1 ���S��I<br>\n";
				$RACELOG.="$name1 ���I �����؂�܂����I �������̂� $name1�I<br>\n";
				}
				else
				{
				$RACELOG.="$name1 �����L����I<br>\n";
				$RACELOG.="$name1�I ���̗��͋����I �������̂� $name1�I<br>\n";
				}
			}
		elsif ($no == $RD[1]->{no})
			{
			# �Q��
			$RACELOG.="���� �ǂ��� ";
			$RACELOG.="$name1 ���ǂ��グ��<br>\n";
			$RACELOG.="$name2 �������� ���̂܂ܓ����؂邩<br>\n";
			if ($RD[1]->{time} - $RD[0]->{time} < 15)
				{
				$RACELOG.="$name1 ������I $name2 ���S��I<br>\n";
				$RACELOG.="$name1 ���������I<br>\n";
				$RACELOG.="$name2 ����y�΂��I �������̂� $name1�I<br>\n";
				}
				else
				{
				$RACELOG.="$name1 ���������I<br>\n";
				$RACELOG.="$name1 ����ɍ����L����I<br>\n";
				$RACELOG.="$name1�I ���̗��͋����I �������̂� $name1�I<br>\n";
				}
			}
		else
			{
			# �g�b�v���S���
			$RACELOG.="���� �ǂ��� ";
			$RACELOG.="$name2 ���������I<br>\n";
			$RACELOG.="����� <b>$name1</b> ����ɑ����I<br>\n";
			if ($RD[1]->{time} - $RD[0]->{time} < 15)
				{
				$RACELOG.="$name1 ������I $name2 ���S��I<br>\n";
				$RACELOG.="$name1 ���������I<br>\n";
				$RACELOG.="$name2 ����y�΂��I �������̂� $name1�I<br>\n";
				}
				else
				{
				$RACELOG.="$name1 ����C�ɍ������I<br>\n";
				$RACELOG.="$name1 ����ɍ����L����I<br>\n";
				$RACELOG.="$name1�I ���̗��͋����I �������̂� $name1�I<br>\n";
				}
			}

	ReadDragon();
	ReadJock();
	ReadRanch();
	ReadStable();

	# �g�b�v
	PushDraLog($rcode+1,$R[0]."�Łu".$RD[0]->{name}."�v�������܂����B");

	my $id=$RD[0]->{dr};
	if (defined $id2dra{$id})
		{
		my $i=$id2dra{$id};
		$DR[$i]->{gr}+=80;
		$DR[$i]->{prize}+=$R[6];

		WritePayLog($DR[$i]->{town},$DR[$i]->{owner},$R[6]*10000);

		if ($R[1] > 2) { $DR[$i]->{sdwin}++;}
		elsif ($R[1]==2) { $DR[$i]->{g3win}++;}
		elsif ($R[1]==1) { $DR[$i]->{g2win}++;}
		else { $DR[$i]->{g1win}++;}
		}

	# �g�b�v�R��
	my $id=$RD[0]->{jock};
	if (defined $id2jk{$id})
		{
		my $i=$id2jk{$id};
		$JK[$i]->{sp}=int(rand(scalar @JKSP)) if !$JK[$i]->{sp};

		#�Ƃ������ɉ����Ĕ\�͏㏸
		if ($RD[0]->{str} > 1)
			{
			$JK[$i]->{back}+=15;
			$JK[$i]->{back}=100 if ($JK[$i]->{back} > 100);
			}
			else
			{
			$JK[$i]->{ahead}+=15;
			$JK[$i]->{ahead}=100 if ($JK[$i]->{ahead} > 100);
			}
		if ($R[1] > 2) { $JK[$i]->{sdwin}++;}
		elsif ($R[1]==2) { $JK[$i]->{g3win}++;}
		elsif ($R[1]==1) { $JK[$i]->{g2win}++;}
		else { $JK[$i]->{g1win}++;}
		}

	# �g�b�v�q��
	my $id=$RD[0]->{ranch};
	if (defined $id2rc{$id})
		{
		my $i=$id2rc{$id};
		$RC[$i]->{prize}+=$R[6];
		if ($R[1] > 2) { $RC[$i]->{sdwin}++;}
		elsif ($R[1]==2) { $RC[$i]->{g3win}++;}
		elsif ($R[1]==1) { $RC[$i]->{g2win}++;}
		else { $RC[$i]->{g1win}++;}
		}

	# �g�b�v�X��
	my $id=$RD[0]->{stable};
	if (defined $id2st{$id})
		{
		my $i=$id2st{$id};
		$ST[$i]->{tr}+=int(rand(20));
		$ST[$i]->{tr}=100 if ($ST[$i]->{tr} > 100);
		$ST[$i]->{con}+=int(rand(20));
		$ST[$i]->{con}=100 if ($ST[$i]->{con} > 100);
		$ST[$i]->{wt}+=int(rand(20));
		$ST[$i]->{wt}=100 if ($ST[$i]->{wt} > 100);

		if ($R[1] > 2) { $ST[$i]->{sdwin}++;}
		elsif ($R[1]==2) { $ST[$i]->{g3win}++;}
		elsif ($R[1]==1) { $ST[$i]->{g2win}++;}
		else { $ST[$i]->{g1win}++;}
		}

	# �Q��
	my $id=$RD[1]->{dr};
	if (defined $id2dra{$id})
		{
		my $i=$id2dra{$id};
		$DR[$i]->{gr}+=40;
		$DR[$i]->{prize}+=$R[7];

		WritePayLog($DR[$i]->{town},$DR[$i]->{owner},$R[7]*10000);
		}

	# �Q���q��
	my $id=$RD[1]->{ranch};
	if (defined $id2rc{$id})
		{
		my $i=$id2rc{$id};
		$RC[$i]->{prize}+=$R[7];
		}

	# �R��
	my $id=$RD[2]->{dr};
	if (defined $id2dra{$id})
		{
		my $i=$id2dra{$id};
		$DR[$i]->{gr}+=20;
		$DR[$i]->{prize}+=$R[8];

		WritePayLog($DR[$i]->{town},$DR[$i]->{owner},$R[8]*10000);
		}

	# �R���q��
	my $id=$RD[2]->{ranch};
	if (defined $id2rc{$id})
		{
		my $i=$id2rc{$id};
		$RC[$i]->{prize}+=$R[8];
		}

	$RACELOG.="<br>";
	foreach(0..$#RD)
		{
		$RACELOG.=($_ + 1)."�� ".GetRaceTime($RD[$_]->{time});
		$RACELOG.=" ".$STRATE[ $RD[$_]->{str} ]." ";
		$RACELOG.=GetTagImgDra($RD[$_]->{fm},$RD[$_]->{color}).$RD[$_]->{name};
		$RACELOG.=" <small>(".$RD[$_]->{lose}.")</small>" if $_;
		$RACELOG.="<br>";
		my $id=$RD[$_]->{dr};
		if (defined $id2dra{$id})
			{
			my $i=$id2dra{$id};
			$DR[$i]->{race}=0;
			$DR[$i]->{con}-=40;
			$DR[$i]->{con}=0 if ($DR[$i]->{con} < 0);

			$DR[$i]->{wt}-=4;
			$DR[$i]->{wt}=38 if ($DR[$i]->{wt} < 38);
			}
		$id=$RD[$_]->{jock};
		$JK[$id2jk{$id}]->{race}=0 if (defined $id2jk{$id});

		undef $RD[$_];
		}
	WriteDragon();
	WriteJock();
	WriteRanch();
	WriteStable();

	$DRTIME[$rcode+1]=$NOW_TIME + 86400 -(($NOW_TIME + $TZ_JST - $DRTIMESET[$rcode+1] * 3600) % 86400);
	$RDS[0]=0;
	$RDS[1]++;
	$RDS[1]=0 if ($RDS[1] > $#MYRACE);
	$RDS[2]=int(rand(2));
}

