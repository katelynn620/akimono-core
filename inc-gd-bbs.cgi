use utf8;
# ギルド掲示板下請け 2003/09/25 由來

sub WriteGBBS
{
	my($msg,$maxlength)=@_;
	return ('','') if !$msg;
	return ($msg,l('発言は半角%1文字(全角%2文字)までです。現在半角%3文字です。',$maxlength,int($maxlength/2),length($msg)).'<br>')
		if length($msg)>$maxlength;
	
	# require $JCODE_FILE;
	# my $msg=CutStr(jcode::sjis($msg,$CHAR_SHIFT_JIS&&'sjis'),$maxlength);
	my $msg=CutStr($msg,$maxlength);
	$msg=~s/&/&amp;/g;
	$msg=~s/>/&gt;/g;
	$msg=~s/</&lt;/g;
	
	my $count=0;
	my $wait=0;
	my $lasttm=0;
	ReadBoard();
	foreach(@MESSAGE)
	{
		my($tm,$mode,$dummy,$id,$msgline,$no)=split(/,/);
		($msgline)=split(/\t/,$msgline);
		next if $DT->{id}!=$id;
		return ('',l('重複投稿は出来ません。').'<br>') if $tm>$NOW_TIME-60*15 && $msgline eq $msg;
		$count++,$wait+=3**$count/($NOW_TIME-$tm+1) if $SECURE_MODE_BBS && $count<10;
		$lasttm||=$tm;
	}
	$wait=int($lasttm+$wait-$NOW_TIME);
	return ('',l('連続投稿は出来ません。あと%1秒お待ち下さい。',$wait).'<br>') if $wait>0;
	
	CoLock();
	WriteBoard(20,0,0,$msg,1) if $MASTER_USER;
	WriteBoard($DT->{icon},$TOWN_TITLE,$DT->{id},$msg."\t".$DT->{shopname}."\t".$DT->{name},1) if !$MASTER_USER;
	CoDataCA();
	CoUnLock();
	return ('','');
}

sub WriteBoard
{
	my($mode,$from,$to,$msg,$nolock)=@_;
	my @data=();
	CoLock() if !$nolock;

	open(IN,"<:encoding(UTF-8)",GetPath($COMMON_DIR,$LOG_FILE));
	@data=<IN>;
	close(IN);
	
	my $no=(split(/,/,$data[0]))[5]+1;
	$no=1 if $no>scalar(@data)*2;
	unshift(@data,"$NOW_TIME,$mode,$from,$to,$msg,$no\n");
	$MAX_BBS_MESSAGE=20 if !$MAX_BBS_MESSAGE;
	splice(@data,$MAX_BBS_MESSAGE);

	OpenAndCheck(GetPath($COTEMP_DIR,$LOG_FILE));
	print OUT @data;
	close(OUT);
	CoDataCA(),CoUnLock() if !$nolock;
}
1;
