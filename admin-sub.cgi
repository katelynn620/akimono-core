use utf8;
# 個別ユーザー管理 2005/03/30 由來

# require $JCODE_FILE;
Lock();
DataRead();
CheckUserPass();
OutError('') if !$MASTER_USER || $USER ne 'soldoutadmin';

OutError(l('ユーザが見つかりません')) if !defined($name2idx{$Q{user}});
my $DT=$DT[$name2idx{$Q{user}}];

# $Q{comment}="【".jcode::sjis($Q{comment})."】" if $Q{comment} ne '';
$Q{comment}="【".$Q{comment}."】" if $Q{comment} ne '';

#重複登録自動アクセス制限の個別対応
if($Q{nocheckip})
{
	$disp.=l('重複登録チェック対象外としました'),$DT->{nocheckip}=1 if $Q{nocheckip} eq 'nocheck';
	$disp.=l('重複登録チェック対象としました'),$DT->{nocheckip}='' if $Q{nocheckip} eq 'check';
}

#アクセス制限制御
if($Q{blocklogin})
{
	# $Q{blocklogin}=jcode::sjis($Q{blocklogin});
	if($Q{blocklogin} eq 'off')
	{
		$disp.=l('アクセス制限を解除しました');
		$DT->{blocklogin}='';
		$DT->{lastlogin}=$NOW_TIME;
	}
	elsif($Q{blocklogin} eq 'stop')
	{
		$disp.=l('経営休止に設定しました[%1]',$Q{blocklogin});
		$DT->{blocklogin}=$Q{blocklogin};
	}
	elsif($Q{blocklogin} ne '')
	{
		$disp.=l('アクセス制限をしました[%1]',$Q{blocklogin});
		$DT->{blocklogin}=$Q{blocklogin};
	}
}

#追放
if($Q{closeshop} eq 'closeshop')
{
	CloseShop($DT->{id},l('追放'));
	PushLog(1,0,l('%1%2は追放されました。',$Q{comment},$DT->{shopname})) if (!$Q{log});

	$disp.=l('追放完了');
	$DTblockip=$DT->{remoteaddr};
}

#賞品授与(デバッグにも使用できます)
if($Q{senditem})
{
	my $itemno=$Q{senditem};
	my $ITEM=$ITEM[$itemno];
	my $itemcount=$Q{count};
	$itemcount+=$DT->{item}->[$itemno-1];
	$itemcount=$ITEM->{limit} if $itemcount>$ITEM[$itemno]->{limit};
	$DT->{item}->[$itemno-1]=$itemcount;
	
	PushLog(2,0,l('%1%2に%3が贈られました。',$Q{comment},$DT->{shopname},$ITEM->{name})) if $Q{comment};
	$disp.=l('%1 %2%3 賞品授与完了',$ITEM->{name},$Q{count},$ITEM->{scale});
}

#賞金授与(デバッグにも使用できます)
if($Q{sendmoney})
{
	$DT->{money}+=$Q{sendmoney};
	#$DT->{saletoday}+=$Q{sendmoney};
	
	PushLog(2,0,l('%1%2に賞金が贈られました。',$Q{comment},$DT->{shopname})) if $Q{comment};
	$disp.=l('%1 賞金授与完了',GetMoneyString($Q{sendmoney}));
}

#持ち時間授与(デバッグにも使用できます)
if($Q{sendtime})
{
	$disp.=l('%1時間 持ち時間授与完了',$Q{sendtime});
	$Q{sendtime}=$Q{sendtime} * 3600;
	$DT->{time}-=$Q{sendtime};
	
	PushLog(2,0,l('%1%2に「%3」が贈られました。',$Q{comment},$DT->{shopname},GetTime2HMS($Q{sendtime}))) if $Q{comment};
}

#爵位授与(デバッグにも使用できます)
if($Q{senddig})
{
	$disp.=l('%1ポイント 爵位経験値授与完了',$Q{senddig});
	$DT->{dignity}+=$Q{senddig};
	
	PushLog(2,0,l('%1%2に爵位経験値%3ポイントが贈られました。',$Q{comment},$DT->{shopname},$Q{senddig}+0)) if $Q{comment};
}

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

$disp=l('行いたい処理とそのパラメータを正しく選択/記述してください') if $disp eq '';
$disp.=" <-- $DT->{shopname} [$DT->{name}] $Q{comment}";

$NOMENU=1;
$Q{bk}="none";
OutSkin();
1;
