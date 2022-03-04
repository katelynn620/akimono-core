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
}

sub l {
    my $i18n = I18N->get_handle('tw');
    return $i18n->maketext(@_);
}

1;