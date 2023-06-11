"""
Implement the Diffie-Hellman Key Exchange mechanism using HTML and JavaScript. Consider the end user as one of the parties (Alice) and the JavaScript application as other party (bob).
"""
# Simple Diffie Hellman

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Diffie-Hellman</title>
</head>
<body>
    <script>
        var G = prompt("Enter G: ")
        var N = prompt("Enter N: ")
        var x = prompt("Enter x: ")
        var y = prompt("Enter y: ")

        function calc(p,q,r){
            return (Math.pow(p,q))%r}

        var A=calc(G,x,N)
        var B=calc(G,y,N)

        var key1=calc(B,x,N)
        var key2=calc(A,y,N)

        if(key1==key2){
            alert("Key is: "+key1)}
        else{
            alert("Key is not same")}
    </script>    
</body>
</html>
