# guild �v���O�C�� 2005/03/30 �R��

sub ReadGuildData
{
	undef %GUILD_DATA;
	open(IN,GetPath($GUILDBAL_FILE));
	while(<IN>)
	{
		chop;
		@_=split(/\t/,$_,2);
		$GUILD_DATA{$_[0]}={split(/\t/,$_[1])};
	}
	close(IN);
}

sub WriteGuildData
{
	OpenAndCheck(GetPath($TEMP_DIR,$GUILDBAL_FILE));
	foreach(keys(%GUILD))
	{
		print OUT $_."\t".join("\t",%{$GUILD_DATA{$_}})."\n";
	}
	close(OUT);
}

sub EditGuildMoney
{
	my($guildcode,$money)=@_;
	my $guild=$GUILD_DATA{$guildcode};
	$guild->{in} += $money if $money>0;
	$guild->{out}+=-$money if $money<0;
	$guild->{money}+=$money;
}

sub CheckGuild
{
	my $dt1guild=$_[0]->{guild};
	my $dt2guild=$_[1]->{guild};
	my $price=$_[2];
	my $margin=0;
	my $rate=1000;
	my $type=0; # 0:�Е�or�o���M���h������ 1:���M���h 2:�كM���h -1:�⏕���s��
	
	if($dt1guild ne '' && $dt2guild ne '')
	{
		$type=$dt1guild eq $dt2guild ? 1 : 2;
		my $guildrate=$GUILD{$dt2guild}->[$GUILDIDX_dealrate];
		$rate+=$type==1 ? -$guildrate : $guildrate;
		$margin=int($price*$guildrate/1000);
		ReadGuildData() if !defined(%GUILD_DATA);
		if($margin)
		{
			$type=-1,$margin=0 if ($type==1 && $GUILD_DATA{$dt1guild}->{money} < 10000);
		}
	}
	return($type,$rate,$margin);
	#return (�M���h�������,������z�{��,����/�����z)
}


1;
