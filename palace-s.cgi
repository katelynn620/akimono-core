use utf8;
# 宮殿達成処理 2004/01/20 由來

Lock();
RequireFile("inc-palace.cgi");
$image[0]=GetTagImgKao(l("王様"),"king",'align="left" ');
$image[1]=GetTagImgKao(l("大臣"),"minister",'align="left" ');

DataRead();
CheckUserPass();

$evt=GetTownData('evt');
$evt=0 if (!$evt);
$level=DignityDefine($DT->{dignity});

$disp.="<BIG>●".l('宮殿')."</BIG><br><br>";

$shopname=$DT->{shopname};
$name=$DT->{name};
$need=$itemno[$evt];

if ( $DT->{item}[$need-1] < $count[$evt] )
	{
	$disp.='<TABLE cellpadding="26" width="570"><tr>';
	$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
	$disp.=$image[0].l('おぉ何ということだ<b>%1</b>の<b>%2%3</b>よ。',$shopname,$name,$level).'<br>';
	$disp.=l('<b>%1%2%3%4</b>は，いまだ揃っていないではないか！',GetTagImgItemType($need),$ITEM[$need]->{name},$count[$evt],$ITEM[$need]->{scale}).'<br>';
	$disp.=l('それとも%1は余をからかっているのではあるまいな？',$name);
	$disp.='<br>'.l('はやく使命を達成するのじゃ。ゆめゆめ忘れるでないぞ。').$TRE;
	$disp.=$TBE."<br>".l('王様はぷりぷり怒り出してしまいました。');
	}
	else
	{
	$disp.='<TABLE cellpadding="26" width="570"><tr>';
	$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
	$disp.=$image[0].l('あっぱれじゃ<b>%1</b>の<b>%2%3</b>よ。',$shopname,$name,$level).'<br>';
	$disp.=l('<b>%1%2%3%4</b>は確かに受け取ったぞ。',GetTagImgItemType($need),$ITEM[$need]->{name},$count[$evt],$ITEM[$need]->{scale}).'<br>';
	$disp.=l('よってそなたに褒美として%1<b>爵位経験値</b>を与えよう。',DignityDefine(1,1)).$TRE;
	$disp.=$TBE."<br>";

	$DT->{item}[$need-1] -= $count[$evt];
	$DT->{dignity}++;
	$evt=int(rand(scalar(@itemno)));
	SetTownData('evt',$evt);

	PushLog(0,0,l('%1が王様の使命を達成しました。',$DT->{shopname}));
	RenewLog();
	DataWrite();
	DataCommitOrAbort();
	}
UnLock();
OutSkin();
1;
