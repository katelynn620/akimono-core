# ��z�֕ҏW 2005/03/30 �R��

my $functionname=$Q{mode};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteDwarf();
DataCommitOrAbort();
UnLock();
1;


sub new
{
	my ($to,$item)=($Q{to},$Q{item});
	OutError("������w�肵�Ă��������B") if $to==-1;
	OutError("�������g�ɑ�z�ւ��o�����Ƃ͂ł��܂���B") if ($to == $DT->{id});
	if ($to==99)
		{
		OutError("�f�Ղ��Ȃ����Ă��Ȃ��̂Ŏw��ł��܂���B") unless -e "trade.cgi";
		$Q{notice}=0;
		}
		else
		{
		OutError("���݂��Ȃ��X�܂ł��B") if !defined($id2idx{$to});
		}
	OutError("�A�C�e���̎w�肪�s���ł��B") if !$ITEM[$item]->{name};
	OutError("�A�C�e���̎w�肪�s���ł��B") if $ITEM[$item]->{flag}=~/r/;	# r �˗��s��

	$Q{num}||=$DT->{item}[$item-1];
	$Q{num}=CheckCount($Q{num},0,0,$DT->{item}[$item-1]);
	OutError("�A�C�e���̍݌ɂ�����܂���B") if !$Q{num};
	my $price=CheckCount($Q{price},0,0,$MAX_MONEY);
	$price=$price * $Q{num} if $Q{unit};
	OutError("�������w�肵�Ă��������B") if !$price;
	my $numrate=$ITEM[$item]->{price} * $Q{num};
	OutError("���i�Ɨ����̉��l���肠���Ă��܂���B") if ($price > $numrate * 2) || ($numrate > $price * 2);

	NoticeDwarf() if $Q{notice};

	@DWF=reverse(@DWF);
	$Dcount++;
	my $i=$Dcount;
	$DWF[$i]->{no}=($i > 0) ? ($DWF[$i-1]->{no} + 1) : 1;
	$DWF[$i]->{tm}=$NOW_TIME;
	$DWF[$i]->{from}=$DT->{id};
	$DWF[$i]->{to}=$to;
	$DWF[$i]->{trade}=(($to==99) ? $DWF[$i]->{no} : "");
	$DWF[$i]->{mode}=1;
	($DWF[$i]->{item},$DWF[$i]->{num},$DWF[$i]->{price})=($item,$Q{num},$price);
	@DWF=reverse(@DWF);

	$DT->{item}[$item-1]-=$Q{num};

	my $cost=0;
	$cost=int($price * $DTTaxrate / 100);
	OutError("�ŋ��𕥂����Ƃ��ł��܂���B") if ($cost > $DT->{money});
	$DT->{taxtoday}+=$cost;
	$DT->{money}-=$cost;

	DataWrite();
	$Q{form}="";
}

sub plus
{
	if ($Q{ng})
	{
		# �󂯎�苑��
		foreach my $i(0..$Dcount)
		{
		next unless $DWF[$i]->{to}==$DT->{id};
		next unless $DWF[$i]->{mode}==1;
		my $act="act_".$DWF[$i]->{no};
		$DWF[$i]->{mode}=3 , next if ($Q{$act});
		}
		return;
	}

	# �󂯎��
	foreach my $i(0..$Dcount)
	{
	next unless $DWF[$i]->{to}==$DT->{id};
	next unless $DWF[$i]->{mode}==1;
	my $act="act_".$DWF[$i]->{no};
	next unless ($Q{$act});
	$DWF[$i]->{mode}=2;
	my ($price,$from,$item,$num)=($DWF[$i]->{price},$DWF[$i]->{from},$DWF[$i]->{item},$DWF[$i]->{num});
	$DT->{paytoday}+=$price;
	$DT->{money}-=$price;
	$DT[$id2idx{$from}]->{money}+=$price;
	$DT[$id2idx{$from}]->{saletoday}+=$price;
	$DT->{item}[$item-1]+=$num;
	$DT->{item}[$item-1]=$ITEM[$item]->{limit} if ($DT->{item}[$item-1]>$ITEM[$item]->{limit});
	}
	OutError("������x�����̂ɕK�v�Ȏ���������܂���B") if ($DT->{money} < 0);
	DataWrite();
}

sub trade
{
	OutError("�f�Ղ��Ȃ����Ă��Ȃ��̂Ŏw��ł��܂���B") unless -e "trade.cgi";
	OutError("�f�Օi���w�肵�Ă��������B") if !defined($Q{code});

	my($boxno,$item,$num,$price)=split(/:/,$Q{code});
	OutError("�A�C�e���̎w�肪�s���ł��B") if !$ITEM[$item]->{name};
	OutError("�A�C�e���̎w�肪�s���ł��B") if $ITEM[$item]->{flag}=~/r/;	# r �˗��s��

	$num=CheckCount($num,0,0,$MAX_MONEY);
	OutError("���̎w�肪�s���ł��B".$num) if !$num;
	$price=CheckCount($price,0,0,$MAX_MONEY);
	OutError("�����̎w�肪�s���ł��B") if !$price;
	OutError("�������������Ă����Ă��������B") if $price > $DT->{money};
	OutError("���̖f�Օi�͂��łɔ���ςł��B") if grep($_->{trade} eq $boxno,@DWF);

	@DWF=reverse(@DWF);
	$Dcount++;
	my $i=$Dcount;
	$DWF[$i]->{no}=($i > 0) ? ($DWF[$i-1]->{no} + 1) : 1;
	$DWF[$i]->{tm}=$NOW_TIME;
	$DWF[$i]->{from}=99;
	$DWF[$i]->{to}=$DT->{id};
	$DWF[$i]->{trade}=$boxno;
	$DWF[$i]->{mode}=0;
	($DWF[$i]->{item},$DWF[$i]->{num},$DWF[$i]->{price})=($item,$num,$price);
	@DWF=reverse(@DWF);
}

sub delete
{
	$WriteMode=0;
	foreach my $i(0..$Dcount)
	{
	next unless $DWF[$i]->{from}==$DT->{id};
	my $act="del_".$DWF[$i]->{no};
	next unless ($Q{$act});
	if ($DWF[$i]->{mode}!=2)	# ���ς݂Ȃ�ԋp�̕K�v�Ȃ�
		{
		$WriteMode=1;
		my ($item,$num)=($DWF[$i]->{item},$DWF[$i]->{num});
		$DT->{item}[$item-1]+=$num;
		$DT->{item}[$item-1]=$ITEM[$item]->{limit} if ($DT->{item}[$item-1]>$ITEM[$item]->{limit});
		}
	undef $DWF[$i];
	}
	DataWrite() if $WriteMode;
}

sub WriteDwarf
{
	undef @RECDWF;	# �ۑ��ƍĒ�`�𓯎���
	undef @SENDWF;
	$NeverD=0;
	my @buf;
	foreach my $i(0..$Dcount)
		{
		next unless defined($DWF[$i]->{no});
		$buf[$i]=join(",",map{$DWF[$i]->{$_}}@DWFnamelist)."\n";
		if ($DWF[$i]->{to}==$DT->{id})
			{
			push(@RECDWF, $i);
			$NeverD++ if $DWF[$i]->{mode}==1;
			}
		push(@SENDWF, $i) if ($DWF[$i]->{from}==$DT->{id});
		}
	OpenAndCheck(GetPath($TEMP_DIR,"dwarf"));
	print OUT @buf;
	close(OUT);
}

sub NoticeDwarf
{
	ReadLetter();

	@LETTER=reverse(@LETTER);
	$Lcount++;
	my $i=$Lcount;
	$LETTER[$i]->{no}=($i) ? ($LETTER[$i-1]->{no} + 1) : 1 ;
	$LETTER[$i]->{time}=$NOW_TIME;
	$LETTER[$i]->{fromt}=$MYDIR;
	$LETTER[$i]->{fromid}=1;
	$LETTER[$i]->{tot}=$MYDIR;
	$LETTER[$i]->{toid}=$Q{to};
	$LETTER[$i]->{title}="��z�֓����̂��m�点";
	$LETTER[$i]->{msg}="������h���[�t��z�ւł��B".$DT->{shopname}."������C����͂����܂����̂ŁC���m�F�����肢�������܂��B";
	$LETTER[$i]->{mode}=1;	#���ǐݒ�
	$LETTER[$i]->{other}=$DT->{shopname};
	@LETTER=reverse(@LETTER);

	WriteLetter();
	CoDataCA();
	CoUnLock();
}

