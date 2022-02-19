# market �v���O�C�� 2003/07/19 �R��

sub GetMarketStatus
{
	undef %marketitemlist;
	
	my($ITEM,$stock,$price,$mpl,$mph,$popular,$uppoint);
	
	foreach(@ITEM)
	{
		$ITEM=$_;
		$ITEM->{todaystock}=
		$ITEM->{todayprice}=
		$ITEM->{todaysale}=
		$ITEM->{yesterdaysale}=
		$ITEM->{marketprice}=
		$ITEM->{uppoint}=
		0;
	}
	
	foreach my $DT (@DT)
	{
		foreach my $caseno (0..$DT->{showcasecount}-1)
		{
			$_=$DT->{showcase}[$caseno];
			$stock=$DT->{item}[$_-1];
			next if !$_ || !$stock;
			$ITEM=$ITEM[$_];
			$ITEM->{todaystock}+=$stock;							# ��݌Ƀg�[�^��
			$price=$DT->{price}[$caseno];
			$ITEM->{todayprice}+=$price*$stock;						# ����z�g�[�^��
			$mpl=\$ITEM->{marketpricelow};
			$mph=\$ITEM->{marketpricehigh};
			$$mpl=$price if $$mpl>$price || !$$mpl;	#�ň��l
			$$mph=$price if $$mph<$price;			#�ō��l
			$marketitemlist{$_}=$ITEM;
		}
		while(my($key,$value)=each %{$DT->{itemtoday}})
		{
			$ITEM=$ITEM[$key];
			$ITEM->{todaysale}+=$value;						# �������㐔
			#$marketitemlist{$key}=$ITEM;				#�J�E���g�Ƃ���
		}
		while(my($key,$value)=each %{$DT->{itemyesterday}})
		{
			$ITEM=$ITEM[$key];
			$ITEM->{yesterdaysale}+=$value;					# �O�����㐔
			# $marketitemlist{$key}=$ITEM;  			#�J�E���g�Ƃ���
		}
	}
	
	my $seed=$DTpeople*$SALE_SPEED/3/50;
	foreach my $ITEM (values %marketitemlist)
	{
		$stock=$ITEM->{todaystock};
		$popular=$ITEM->{popular};
		$uppoint=!$popular ? 100 : int($stock/$seed*$popular);
		$uppoint=10   if $uppoint<10;
		$uppoint=1000 if $uppoint>1000;
		
		$ITEM->{marketprice}=int($ITEM->{todayprice}/$stock) if $stock;
		
		$ITEM->{uppoint}=$uppoint;
	}
}

# ���v/�����o�����X�O���t
sub GetMarketStatusGraph
{
	my($per,$noimage)=@_;
	my $ret="";
	my $width=100;
	my $type=0;
	
	$width=int($per>1000?$width:int($per*$width/1000)),$type=1 if $per>=110;
	$width=int((100-$per+10)*$width/100),$type=2 if $per<=90;
	
	my $imgwidth=int($width/2);
	my $imgwidthl=$type==1 ? 50 : 50-$imgwidth;
	my $imgwidthr=$type==2 ? 50 : 50-$imgwidth;
	
	if(!$MOBILE && !$noimage)
	{
		if($type)
		{
			$ret.=qq|<img src="$IMAGE_URL/t.gif" width="$imgwidthl" height="12">| if $imgwidthl;
			$ret.=" �O�a " if $imgwidthl==50;
			$ret.=qq|<img src="$IMAGE_URL/|.('b','r')[$type-1].qq|.gif" width="$imgwidth" height="12">|;
			$ret.=" �s�� " if $imgwidthr==50;
			$ret.=qq|<img src="$IMAGE_URL/t.gif" width="$imgwidthr" height="12">| if $imgwidthr;
		}
		else
		{
			$ret.=qq|<img src="$IMAGE_URL/t.gif" width="50" height="12"> �ύt |;
			$ret.=qq|<img src="$IMAGE_URL/t.gif" width="50" height="12">|;
		}
	}
	else
	{
		$width=!$type ? "" : " $width%";
		$ret.=('�ύt ','�O�a ','�s�� ')[$type].$width;
	}
	return $ret;
}


1;
