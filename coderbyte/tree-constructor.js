function TreeConstructor(strArr) {
    let newStrArr = [];
    strArr.forEach(i => {
        // '(1,2)' -> [1,2]
        let a = parseInt(i.split(',')[0].slice(1));
        let b = parseInt(i.split(',')[1].slice(0, -1));
        newStrArr.push([a, b]);
    })
    strArr = newStrArr;

    const children = [];
    const parents = [];
    strArr.forEach(i => {
        children.push(i[0]);
        parents.push(i[1]);
    })
    function oneRoot() {
        const roots = [];
        parents.forEach(i => {
            if (!children.includes(i)) roots.push(i);
        })
        return new Set(roots).size === 1;
    }

    function oneParent() {
        return children
            .map(i => children.filter(x => x === i).length)
            .every(k => k === 1);
    }

    function atLeastTwoChildren() {
        return parents
            .map(i => parents.filter(x => x === i).length)
            .every(k => k <= 2);
    }

    if (!oneRoot()) {
        console.log('not one root');
        return false;
    }
    else if (!oneParent()) {
        console.log('not one parent');
        return false;
    }
    else if (!atLeastTwoChildren()) {
        console.log('more than two children');
        return false;
    }
    else {
        return true;
    }
}

console.log(TreeConstructor(["(10,20)"]));