document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM is fully loaded");

    // フォームの取得
    const reservationForm = document.getElementById('reservationForm');
    console.log("reservationForm found:", reservationForm);

    // フォームが見つかれば submit イベントリスナーを追加
    if (reservationForm) {
        reservationForm.onsubmit = function(event) {
            console.log("Form submission event triggered");

            const timeInput = document.getElementById('reservation_time').value;
            console.log("Selected time:", timeInput);

            const minTime = "12:00";
            const maxTime = "21:00";

            // 時間文字列を Date オブジェクトに変換
            const inputTime = new Date(`1970-01-01T${timeInput}:00`);
            const minimumTime = new Date(`1970-01-01T${minTime}:00`);
            const maximumTime = new Date(`1970-01-01T${maxTime}:00`);

            // 入力時間のバリデーション
            if (inputTime < minimumTime || inputTime > maximumTime) {
                console.log("Validation failed: Time is out of range");
                alert("Please select a time between 12:00 and 21:00.");
                event.preventDefault();  // フォーム送信をキャンセル
            } else {
                console.log("Validation passed");
            }
        };
    }
});


