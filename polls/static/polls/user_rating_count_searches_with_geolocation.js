export function createMarkers(map, restaurants, infoWindow) {
    let beachFlagImg;
    const intersectionObserver = new IntersectionObserver((entries) => {
            for (const entry of entries) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("drop");
                    intersectionObserver.unobserve(entry.target);
                }
            }
        });

    // Create the markers.
    restaurants.forEach(({
                             position,
                             title,
                             google_maps_uri,
                             primary_type_display_name,
                             rating,
                             business_status,
                             user_rating_count,
                             beach_flag_img_src
                         }, i) => {
        //////////////////////////////////////////////////////
        // マーカーの画像を作成
        //////////////////////////////////////////////////////
        beachFlagImg = document.createElement("img");
        beachFlagImg.src = beach_flag_img_src;
        beachFlagImg.style.width = "80px"; // 画像のサイズ調整
        beachFlagImg.style.height = "80px"; // 画像のサイズ調整
        beachFlagImg.style.borderRadius = "50%"; // 丸い形にする
        const marker = new google.maps.marker.AdvancedMarkerView({
            position,
            map,
            content: beachFlagImg,
        });

        //////////////////////////////////////////////////////
        // マーカーのアニメーションを設定
        //////////////////////////////////////////////////////
        const element = marker.content;

        element.style.opacity = "0";
        element.addEventListener("animationend", (event) => {
            element.classList.remove("drop");
            element.style.opacity = "1";
        });

        const time = 1 + Math.random(); // 1s delay for easy to see the animation

        element.style.setProperty("--delay-time", time + "s");
        intersectionObserver.observe(element);

        //////////////////////////////////////////////////////
        // マーカーがクリックされたときの処理
        //////////////////////////////////////////////////////
        marker.addListener("gmp-click", () => {
            infoWindow.close();
            const detail_content = document.createElement("div");

            // Bootstrap用のカードデザインを適用
            detail_content.classList.add("card");
            detail_content.style.maxWidth = "100%";  // 幅をスマホでも収まるように100%に設定
            detail_content.style.margin = "0 auto";  // カードが中央に表示されるように調整

            // 画像部分にBootstrapのカードクラスを追加
            const imageElement = document.createElement("img");
            imageElement.src = beach_flag_img_src;
            imageElement.classList.add("card-img-top");  // カードのトップ画像にする
            imageElement.style.objectFit = "cover";  // 画像のアスペクト比を維持
            imageElement.style.height = "150px";  // 画像の高さをスマホでも適切に表示されるように設定
            detail_content.appendChild(imageElement);

            // カードの本文部分を作成
            const cardBody = document.createElement("div");
            cardBody.classList.add("card-body", "p-2");  // パディングを小さくしてコンテンツが詰まるのを防ぐ

            // 店舗のタイトルを表示 (Bootstrapのクラスを使って強調)
            const nameElement = document.createElement("h5");
            nameElement.classList.add("card-title");
            nameElement.textContent = title;
            cardBody.appendChild(nameElement);

            // 店舗の種類を表示
            const placeTypeElement = document.createElement("p");
            placeTypeElement.classList.add("card-text");
            placeTypeElement.textContent = primary_type_display_name;
            cardBody.appendChild(placeTypeElement);

            // 営業状態を表示
            const placeBusinessStatusElement = document.createElement("p");
            placeBusinessStatusElement.classList.add("card-text");
            if (business_status === "OPERATIONAL") {
                placeBusinessStatusElement.textContent = "営業中";
                placeBusinessStatusElement.classList.add("text-success");
            } else if (business_status === "CLOSED_TEMPORARILY") {
                placeBusinessStatusElement.textContent = "一時休業中";
                placeBusinessStatusElement.classList.add("text-warning");
            } else if (business_status === "CLOSED_PERMANENTLY") {
                placeBusinessStatusElement.textContent = "閉店済み";
                placeBusinessStatusElement.classList.add("text-danger");
            }
            cardBody.appendChild(placeBusinessStatusElement);

            // 評価を表示
            const placeRatingElement = document.createElement("p");
            placeRatingElement.classList.add("card-text");
            // 星のアイコンを表示
            const starIcon = document.createElement("i");
            starIcon.classList.add("bi-star");
            placeRatingElement.appendChild(starIcon);

            // 評価の数値を表示
            const ratingText = document.createTextNode(`  ${rating}`);
            placeRatingElement.appendChild(ratingText);
            cardBody.appendChild(placeRatingElement);

            // レビュー数を表示
            const placeUserRatingCountElement = document.createElement("p");
            placeUserRatingCountElement.classList.add("card-text");
            // コメントアイコンを表示
            const commentIcon = document.createElement("i");
            commentIcon.classList.add("bi-chat-left");
            placeUserRatingCountElement.appendChild(commentIcon);

            // レビュー数の数値を表示
            const reviewText = document.createTextNode(`  ${user_rating_count}`);
            placeUserRatingCountElement.appendChild(reviewText);
            cardBody.appendChild(placeUserRatingCountElement);

            // 「Google Mapsで見る」リンクを挿入
            const placeUrlElement = document.createElement("a");
            placeUrlElement.href = google_maps_uri;
            placeUrlElement.target = "_blank";
            placeUrlElement.textContent = "Google Mapsで見る";
            placeUrlElement.classList.add("btn", "btn-secondary", "btn-sm", "mt-2");  // スマホ向けに小さいボタンにする
            cardBody.appendChild(placeUrlElement);

            // カード本文を詳細コンテンツに追加
            detail_content.appendChild(cardBody);

            // infoWindowにセットして開く
            infoWindow.setContent(detail_content);
            infoWindow.open(marker.map, marker);
        });
    });
}
