var packageList = document.getElementById('package-list');
packages.map(function (pkg) {
    var packageItem = document.createElement('li');
    var packageName = document.createTextNode(pkg);
    packageItem.appendChild(packageName);
    packageList.appendChild(packageItem);
})