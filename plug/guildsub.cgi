# guildsub �v���O�C�� 2003/11/03 �R��

sub ReadGuild
{
	my($code)=@_;
	
	undef %GUILD_DETAIL;
	
	my @guildlist=GetGuildDirFiles();
	
	return "" if !scalar(@guildlist);
	
	foreach my $code (@guildlist)
	{
		my @data=ReadConfig($COMMON_DIR."/".$code.".pl");	#�M���h�t�@�C���̂݊g���q�ύX
		$GUILD_DETAIL{$code}={'code',$code,@data} if scalar(@data);
	}
	
	return ($code ne '' ? $GUILD_DETAIL{$code} : "");
}

sub GetGuildDirFiles
{
	opendir(DIR,$COMMON_DIR);
	my $FILE_PL='.pl';	#�M���h�t�@�C���̂݊g���q�ύX
	my @guildlist=sort map{/^(\w+)$FILE_PL$/} grep(/^\w+$FILE_PL$/,readdir(DIR));
	closedir(DIR);
	return @guildlist;
}

sub MakeGuildFile
{
	my @guildlist=GetGuildDirFiles();
	
	OpenAndCheck(GetPath($TEMP_DIR,$GUILD_FILE));
	print OUT '$GUILDIDX_name=0;$GUILDIDX_dealrate=1;$GUILDIDX_feerate=2;';
	print OUT '%GUILD=(';
	foreach my $code (keys(%GUILD_DETAIL))
	{
		my $detail=$GUILD_DETAIL{$code};
		print OUT "'$code'=>[";
		print OUT (GetString($detail->{shortname})),",";
		print OUT $detail->{dealrate}.",";
		print OUT $detail->{feerate}.",";
		print OUT "],";
	}
	print OUT ');1;';
	close(OUT);
	
	my %okguild=map{($_,1)}keys(%GUILD_DETAIL);
	foreach my $code (grep(!$okguild{$_},keys(%GUILD)))
	{
		next if $code eq '';
		PushLog(1,0,"�M���h�u".$GUILD{$code}->[$GUILDIDX_name]."�v�͖łт܂����B",1);
		foreach my $DT (@DT)
		{
			$DT->{guild}="",delete $DT->{user}{_so_e} if ($DT->{guild} eq $code);
		}
	}
	foreach my $code (grep(!$GUILD{$_},keys(%okguild)))
	{
		next if $code eq '';
		PushLog(1,0,"�M���h�u".$GUILD_DETAIL{$code}->{shortname}."�v����������܂����B",1);
	}
}
1;
