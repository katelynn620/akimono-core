{

    package I18N;
    use FindBin qw($Bin);
    use parent 'Locale::Maketext';
    use Locale::Maketext::Lexicon {
        '*'     => [ Gettext => "$Bin/../program/locale/*.po" ],
        _auto   => 1,
        _decode => 1,
        _style  => 'gettext',
    };

    sub fallback_languages {
        return ('ja_JP');
    }
}

sub l {
    my $i18n = ( $LANG ne "" ) ? I18N->get_handle($LANG) : I18N->get_handle();
    return $i18n->maketext(@_);
}

1;
