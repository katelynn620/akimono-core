# �ړ]���� 2004/01/20 �R��

OutError('�g�p�s�ł�') if !$MOVETOWN_ENABLE || !$TOWN_CODE;
my $townmaster=ReadTown($TOWN_CODE,'getown');
OutError('�g�p�s�ł�') if !$townmaster;
DataRead();
CheckUserPass();

OutError('bad request') if  ($Q{towncode} eq '' || $Q{pass} eq '');
OutError('�p�X���[�h������������܂���') if $Q{pass} ne $MASTER_PASSWORD && !CheckPassword($Q{pass},$DT->{pass});

#�ړ]����
$disp.=MoveShop($DT,$Q{towncode});

OutSkin();
1;

sub MoveShop
{
	my($DT,$towncode)=@_;
	
	my($town)=ReadTown($towncode);
	return '<b>�ړ]�\�ȊX��������܂���</b>' if !$town;
	return '<b>�ړ]��ł̖��O���s���ł�(12�����ȓ�)</b>' if $Q{name} eq '' || length $Q{name}>12 || $Q{name}=~ /([,:;\t\r\n<>&])/;
	
	$DT->{newname}=$Q{name};
	$DT->{newpass}=$Q{pass};
	$DT->{remoteaddr}=GetTrueIP();
	
	require "$ITEM_DIR/funcshopout.cgi" if $DEFINE_FUNCSHOPOUT;
	
	$DT->{_MoveTownTimeSrc}=GetMoveTownTime($DT,$townmaster,$town);
	
	MakeMoveDT($DT);
	my $data=GetDataTree($DT);
	my $subdata=ReadSubData($DT);
	#my $datahash=GetHash(time(),$data);
	my $towndata="code\t$TOWN_CODE\tname\t$townmaster->{name}";
	$towndata.="\tgroup\t$townmaster->{group}" if $townmaster->{group} ne '';
	my $trueip=GetTrueIP();
	my $result=PostHTTP($town->{recvshopurl},"$data\n$subdata->{stock}\n$towndata\n$trueip",$townmaster->{password},$TOWN_CODE);
	
	if($result eq 'OK')
	{
		Lock();
		DataRead();
		CheckUserPass();
		PushLog(1,0,$DT->{shopname}."���ړ]���Ă����܂����B");
		CloseShop($DT->{id},$town->{name}."�ֈړ]");
		RenewLog();
		DataWrite();
		DataCommitOrAbort();
		UnLock();
		my $trash="";
		if($GET_DATA{trash})
		{
			@_=split(/\t/,$GET_DATA{trash});
			my($code,$name)=split(/!/,shift);
			my %trashitem=@_; my $val=0;
			foreach(values(%trashitem)){$val+=$_;}
			$trash=$name."�ŕۊǂ��Ă������i ".scalar(keys(%trashitem))." ��� ".$val." ���j������܂����B";
		}
		$MENUSAY='<A HREF="index.cgi" TARGET=_top>[�g�b�v]</A> ';
		SetCookieSession();
		return	$town->{name}."�ֈړ]���܂����B<br>".
				GetTagA($town->{name}."�ֈړ�","action.cgi?key=jump&town=$town->{code}")."<br><br>".$trash;
	}
	elsif($result eq 'DENY')
	{
		return	"�ړ]�����ۂ���܂����B�ړ]��̏󋵂�ړ]�󂯓�������������m�F�������B<br>".
				"<b>$GET_DATA{msg}</b><br>".
				GetTagA($town->{name}."��K��Ă݂�","action.cgi?key=jump&town=$town->{code}","","_blank");
	}
	elsif($result eq 'ERROR')
	{
		return	"�ړ]��ɐڑ��o���܂���ł����B�ړ]��̏󋵂��m�F���A�K�v������Ίe�Ǘ��҂܂ł��A���������B<br>".
				GetTagA($town->{name}."���m�F","action.cgi?key=jump&town=$town->{code}","","_blank");
	}
	else
	{
		return "error code [ $result ]";
	}
}

sub MakeMoveDT
{
	my($DT)=@_;
	$DT->{itemcode}={};
	$DT->{expcode}={};
	$DT->{itemyesterdaycode}={};
	$DT->{itemtodaycode}={};
	my $val;
	foreach my $no (1..$MAX_ITEM)
	{
		my $code=$ITEM[$no]->{code};
		
		$val=$DT->{item}->[$no-1];
		$DT->{itemcode}->{$code}=$val if $val;
		
		$val=$DT->{exp}->{$no};
		$DT->{expcode}->{$code}=$val if $val;
		
		$val=$DT->{itemyesterday}->{$no};
		$DT->{itemyesterdaycode}->{$code}=$val if $val;
		
		$val=$DT->{itemtoday}->{$no};
		$DT->{itemtodaycode}->{$code}=$val if $val;
	}
	$DT->{showcasecode}=[];
	foreach my $idx (0..$DT->{showcasecount}-1)
	{
		my $itemno=$DT->{showcase}->[$idx];
		my $price=$DT->{price}->[$idx];
		$price=0 if !$itemno;
		$DT->{price}->[$idx]=$itemno ? $price : 0;
		$DT->{showcasecode}->[$idx]=$itemno ? $ITEM[$itemno]->{code} : "";
	}
	delete $DT->{showcase};
	#delete $DT->{price};
	delete $DT->{item};
	delete $DT->{exp};
	delete $DT->{itemyesterday};
	delete $DT->{itemtoday};
	
	foreach(grep /^_so_trtm_/,keys %{$DT->{user}})
	{
		delete $DT->{user}{$_};
	}
}

sub PostHTTP
{
	my($url,$query,$password,$header)=@_;
	
	$POSTHTTPERROR=0;
	
	return 'NOURL' if $url eq '';
	
	$url=~/^http:\/\/(.+?)(\/.+)$/;
	my($host,$file)=($1,$2);
	$query=$header."\n".GetHash(time(),$password)."\n".$query;
	my $length=length($query);
	
	# socket open
	my $addr=(gethostbyname($host))[4];
	my $name=pack("S n a4 x8",2,80,$addr);
	return 'NOTOPENSOCKET' if !socket(S,2,1,0);
	return 'NOTCONNECT' if !connect(S,$name);
	binmode(S);
	select(S); $|=1;
	select(STDOUT);
	
	print S join("\r\n",
		(
			"POST $file HTTP/1.0",
			"User-Agent: SOLD OUT($TOWN_CODE)",
			"Host: $host",
			"Referer: http://$host$file",
			"Content-Length: $length",
			"",
			$query
		)
	);
	$SIG{ALRM}=\&SocketTimeOut;
	alarm(60);
	while(<S>){s/[\r\n]//g; last if $_ eq "";}
	$GET_RETURN_CODE=<S>; $GET_RETURN_CODE=~s/[\r\n]//g;
	$GET_DATA="";
	while(<S>){$GET_DATA.=$_;}
	alarm(0);
	close(S);
	
	%GET_DATA=();
	$POSTHTTPERROR=1 if $GET_RETURN_CODE=~/[^A-Z]/;
	if($POSTHTTPERROR)
	{
		$GET_RETURN_CODE='ERROR';
		$GET_DATA='';
		$POSTHTTPERROR=0;
	}
	foreach(split(/\r?\n/,$GET_DATA))
	{
		$GET_DATA{$1}=$2 if /^\s*(.+?)\s*=\s*(.+)\s*$/;
	}
	
	return $GET_RETURN_CODE;
}

sub SocketTimeOut
{
	close(S);
	$POSTHTTPERROR=1;
	return "ERROR";
}
