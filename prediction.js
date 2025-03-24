
    async function fetchPredictions() {
        try {
            const response = await fetch("logs/features.csv");
            const data = await response.text();
            
            const rows = data.split("\n").slice(1); // Skip header
            let tableContent = "";

            rows.forEach(row => {
                const columns = row.split(",");
                if (columns.length > 1) {
                    const activityCode = columns[0];
                    const ipFrequency = columns[1];
                    const userAgent = columns[2];
                    const activityEncoded = columns[3];
                    const hour = columns[4];
                    const day = columns[5];
                    const weekday = columns[6];
                    const prediction = columns[7];

                    // Determine row color based on prediction (Suspicious or Normal)
                    const rowColor = prediction.trim() === "1" ? "#ffcccc" : "#ccffcc";
                    const predictionText = prediction.trim() === "1" ? "Suspicious" : "Normal";

                    tableContent += `
                        <tr style="background-color: ${rowColor};">
                            <td style="padding: 12px; text-align: center;">${activityCode}</td>
                            <td style="padding: 12px; text-align: center;">${ipFrequency}</td>
                            <td style="padding: 12px; text-align: center;">${userAgent}</td>
                            <td style="padding: 12px; text-align: center;">${activityEncoded}</td>
                            <td style="padding: 12px; text-align: center;">${hour}</td>
                            <td style="padding: 12px; text-align: center;">${day}</td>
                            <td style="padding: 12px; text-align: center;">${weekday}</td>
                            <td style="padding: 12px; text-align: center; font-weight: bold; color: ${prediction.trim() === "1" ? "red" : "green"};">${predictionText}</td>
                        </tr>
                    `;
                }
            });

            document.getElementById("predictionTableBody").innerHTML = tableContent;
        } catch (error) {
            console.error("Error fetching predictions:", error);
        }
    }

    // Refresh predictions every 5 seconds
    setInterval(fetchPredictions, 5000);

