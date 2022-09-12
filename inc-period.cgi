use utf8;
# 決算処理 2005/03/30 由來

	foreach(keys(%GUILD))
	{
		$GUILD_DATA{$_}->{in}=0;
		$GUILD_DATA{$_}->{out}=0;
		delete($GUILD_DATA{$_}->{guild});
		unlink($COMMON_DIR."/".$_.".pl") if ($GUILD_DATA{$_}->{money} < 0);
	}
	
	if(defined($DT[0]))
	{
		#その時点でのトップの店のTOPカウンタを+1
		$DT[0]->{rankingcount}++;
		
		#優勝者発表
		my $DT=$DT[0];
		my $count=$DT->{rankingcount}==1 ? l("初優勝") : l("%1度目の優勝",$DT->{rankingcount});
		my $msg=l("「今期の優勝店は%1さんでした。%2おめでとうございます」",$DT->{shopname},$count);
		PushLog(1,0,$msg);
		
		$msg=l("「点数は%1点",$DT->{point});
		$msg.=l("で、2位との差は%1点",($DT->{point}-$DT[1]->{point})) if defined($DT[1]);
		$msg.=l("でした」");
		PushLog(1,0,$msg);
	}
	
	require "$ITEM_DIR/funcupdate.cgi" if $DEFINE_FUNCUPDATE;
	
	#決算時のドラゴンレース収支処理
	DragonBalance();

	#決算時のカスタム処理
	UpdateResetBefore() if defined(&UpdateResetBefore);

	#租税額リセット（領主制）
	my $taxin=0;

	my $dtcount=0;
	foreach my $DT (@DT)
	{
		$dtcount++;
		
		#経営者不在
		if ($NOW_TIME-$DT->{foundation} > 43200 && $DT->{blocklogin} ne 'stop')
		{
			if ($DT->{lastlogin}+$EXPIRE_TIME<$NOW_TIME)
			{
			CloseShop($DT->{id},l('経営者不在'));
			PushLog(1,0,l("%1が経営者不在のため閉店しました。",$DT->{shopname}));
			}
		}

		#ドラゴンレース清算
		if ($DT->{dragon})
			{
			PushLog(0,$DT->{id},l("ドラゴンレースの収支")." ".GetMoneyString($DT->{dragon}));
			$DT->{money}+=$DT->{dragon};
			$DT->{drmoney}+=$DT->{dragon};
			$DT->{saletoday}+=$DT->{dragon} if ($DT->{dragon} > 0);
			$DT->{paytoday}-=$DT->{dragon} if ($DT->{dragon} < 0);
			}

		#前期の情報を保存
		$DT->{rankingyesterday}=$dtcount;
		$DT->{profitstock}=int(($DT->{profitstock}*$PROFIT_DAY_COUNT+$DT->{saletoday}-$DT->{paytoday})/($PROFIT_DAY_COUNT+1));
		$DT->{saleyesterday}=$DT->{saletoday};
		$DT->{saletoday}=0;
		$DT->{payyesterday}=$DT->{paytoday};
		$DT->{paytoday}=0;
		$DT->{itemyesterday}=$DT->{itemtoday};
		$DT->{itemtoday}={};
		$DT->{taxyesterday}=$DT->{taxtoday};
		$DT->{taxtoday}=0;
		
		#所持数オーバーチェック＆不正値修正
		foreach my $cnt (1..$MAX_ITEM)
		{
			$DT->{item}[$cnt-1]=$ITEM[$cnt]->{limit} if $DT->{item}[$cnt-1]>$ITEM[$cnt]->{limit};
			$DT->{item}[$cnt-1]=int($DT->{item}[$cnt-1]);
		}
		
		#維持費徴収処理
		my $cost=int($DT->{costtoday});
		$cost+=$SHOWCASE_COST[$DT->{showcasecount}-1];
		$DT->{money}-=$cost;
		$DT->{paytoday}+=$cost;
		
		#租税収入（領主制）
		$taxin+=$DT->{taxyesterday};

		#ギルド会費
		if($DT->{guild} ne '')
		{
			my $money=int($DT->{saleyesterday}*$GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/1000);
			EditGuildMoney($DT->{guild},$money);
			$DT->{money}-=$money;
						# ギルド攻防自然変動
			$GUILD_DATA{$DT->{guild}}->{atk}=int($GUILD_DATA{$DT->{guild}}->{atk} *24 /25);
			$GUILD_DATA{$DT->{guild}}->{def}=int($GUILD_DATA{$DT->{guild}}->{def} *9 /10);
			$GUILD_DATA{$DT->{guild}}->{def}+=int($money/800);
			$GUILD_DATA{$DT->{guild}}->{def}=1000 if ($GUILD_DATA{$DT->{guild}}->{def}>1000);
		}
		
		$DT->{costyesterday}=$cost;
		$DT->{costtoday}=0;
		
		#熟練度自然減少
		foreach my $key (keys(%{$DT->{exp}}))
		{
			$DT->{exp}{$key}-=int($DT->{exp}{$key}*$EXP_DOWN_RATE/1000) if $EXP_DOWN_RATE;
			$DT->{exp}{$key}-=$EXP_DOWN_POINT;
			delete $DT->{exp}{$key} if $DT->{exp}{$key}<=0;
		}

		#爵位ポイント自然減少
		if ($DT->{dignity} && rand(100) < 25)
		{
			my $i=int( ($DT->{dignity}) / 12) + 1;
			$DT->{dignity}-=$i;
		}
	}
	SortDT();
	
	#領土データ調整
	$STATE->{people}=$DTpeople;	#前期人口を保存。
	$DTpeople=(24000 * $DTusercount) + 100000 + ($STATE->{develop} * 30) + ($STATE->{safety} * 20);	#前期状態で人口決定。
	$STATE->{money}+=$taxin;
	$STATE->{in}=$taxin;
	$STATE->{develop}+=int(($STATE->{devem} / $STATE->{people} * 200) - ($STATE->{develop}/10) - rand(200));	#500万円が標準（20万人）
	$STATE->{safety}+=int(($STATE->{safem} / $STATE->{people} * 200) - ($STATE->{safety}/10) - rand(200));	#500万円が標準（20万人）

	if ($STATE->{army} + $STATE->{robina}< 10000)
		{
		#兵士が少ない場合のペナルティ
		$STATE->{safety}-=int( (10000 - $STATE->{army}- $STATE->{robina}) / 20);
		PushLog(2,0,l("街の護衛軍が少ないため，治安が悪化しています。"));
		}
	$STATE->{develop}=1000 if $STATE->{develop} < 1000;
	$STATE->{safety}=1000 if $STATE->{safety} < 1000;
	my $armycost=200-int($STATE->{safety} / 100);
	$STATE->{out}=($STATE->{army}*$armycost) + $STATE->{devem} + $STATE->{safem};
	$STATE->{money}-=$STATE->{out};
	if ($DTevent{rebel})
		{
		$DTevent{rebel}=$NOW_TIME+86400*3;
		}
		else
		{
		RebelRobin();
		}
	$STATE->{army}+=$STATE->{robina};	# 義勇軍を正規軍に。
	if ($STATE->{money} < 0)
	{
		#給料を払えない
		PushLog(2,0,l("街資金が底をつき，街の護衛軍に給料を支払えないようです。"));
		$STATE->{army}=int($STATE->{army} / 3);
		$STATE->{money}=0;
	}
	if (defined($id2idx{$STATE->{leader}}))
	{
	$STATE->{robina}=0;
	}
	else
	{
	$STATE->{robina}=$STATE->{army};
	$STATE->{army}=0;
	}

	#決算時のカスタム処理（リセット後）
	UpdateResetAfter() if defined(&UpdateResetAfter);
	
	#データバックアップ($BACKUP世代≒$BACKUP期)
	mkdir($BACKUP_DIR.$BACKUP,$DIR_PERMISSION) if !(-e $BACKUP_DIR.$BACKUP);
	rename($BACKUP_DIR.$BACKUP,$BACKUP_DIR."_work");
	foreach my $count (reverse(1..$BACKUP-1))
	{
		mkdir($BACKUP_DIR.$count,$DIR_PERMISSION) if !(-e $BACKUP_DIR.$count);
		rename($BACKUP_DIR.$count,$BACKUP_DIR.($count+1));
	}
	rename($BACKUP_DIR."_work",$BACKUP_DIR."1");
	
	foreach my $filetype (@BACKUP_FILES)
	{
		open(IN,"<:encoding(UTF-8)",GetPath($filetype));
		open(OUT,">:encoding(UTF-8)",GetPath($BACKUP_DIR."1",$filetype));
		while(<IN>){print OUT $_;}
		close(OUT);
		close(IN);
	}
	
	#無効なセッションデータ(期限切れ)を削除
	opendir(SESS,$SESSION_DIR);
	my @dir=readdir(SESS);
	closedir(SESS);
	my $sessiontimeout=$NOW_TIME-$EXPIRE_TIME;
	foreach(map{"$SESSION_DIR/$_"}grep(/^.+\.cgi$/,@dir))
	{
		unlink $_ if (stat($_))[9]<$sessiontimeout; # $EXPIRE_TIME使われなければ消去
	}
	MakeGuildFile();
1;


sub RebelRobin
{
return if !defined($id2idx{$STATE->{leader}});
my $i=int(15000 - $STATE->{develop} - $STATE->{safety} - rand(2500));
my $ii=int(50000000 - $STATE->{money} - rand(5000000));
return if ($i > 1000)&&($ii > 5000000);
PushLog(2,0,l("%1%2が不穏な動きを見せています。",$BAL_JOB,$BAL_NAME)),return if ($i > 0) && ($ii > 0);
if (rand(100) < 30)
	{
	$DTevent{rebel}=$NOW_TIME+86400*3;
	$STATE->{robinb}=10000;
	PushLog(2,0,l("%1%2が街に攻め込み，反乱を起こしました！",$BAL_JOB,$BAL_NAME));
	}
	else
	{
	PushLog(2,0,l("%1%2が攻める時機をうかがっているようです。",$BAL_JOB,$BAL_NAME));
	}
}

sub DragonBalance
{
	my $fn=GetPath($COMMON_DIR,"drapay-".$MYDIR);
	open(IN,"<:encoding(UTF-8)",$fn) or return;
	my @req=<IN>;
	close(IN);
	foreach (0..$#req)
		{
		chop $req[$_];
		my @buf=split(/\t/,$req[$_]);
		next if !defined($id2idx{$buf[0]});
		my $i=$id2idx{$buf[0]};
		$DT[$i]->{dragon}+=$buf[1];
		}
	unlink $fn;
}

