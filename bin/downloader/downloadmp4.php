<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST'){
    $url = (isset($_POST['url1']) && !empty($_POST['url1'])) ? $_POST['url1'] : false;
    if (!$url) {
        echo "Vul alstublieft een url in";
    } else {
        $source = file_get_contents($url);
        $source = urldecode($source);

        // Verkrijg de video titel.
        $vTitle_results_1 = explode('<title>', $source);
        $vTitle_results_2 = explode('</title>', $vTitle_results_1[1]);

        $title = trim(str_replace(' – YouTube', ”, trim($vTitle_results_2[0])));

        // Extract video download URL.
        $dURL_results_1 = explode('url_encoded_fmt_stream_map', "url1=", $source);
        $dURL_results_2 = explode('\u0026quality', $dURL_results_1[1]);

        // Force download van d  video.
        $file = str_replace(' ', '_', strtolower($title)).'.mp4';

        header("Cache-Control: public");
        header("Content-Description: File Transfer");
        header("Content-Disposition: attachment; filename=$file");
        header("Content-Type: video/mp4");
        header("Content-Transfer-Encoding: binary");

        readfile($dURL_results_2[0]);

        exit;
    }
}
?>

