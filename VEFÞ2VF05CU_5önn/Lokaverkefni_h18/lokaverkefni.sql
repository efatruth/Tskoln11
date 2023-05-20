drop  DATABASE 0301865919_lokaverkefni;
create DATABASE 0301865919_lokaverkefni;
USE 0301865919_lokaverkefni;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dsg_prufa`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

drop table notandur;

   CREATE TABLE `notandur` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `email` varchar(255) COLLATE utf8_bin NOT NULL,
        `password` varchar(255) COLLATE utf8_bin NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
    AUTO_INCREMENT=1 ;




--
-- Dumping data for table `user`
--

INSERT INTO `notandur` (`id`, `email`, `password`) VALUES
("0401901234",'daniel@yahoo.com', 'danielpassword'),
("1002942468",'john@yahoo.com', 'johnpassword');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

select * from notendur;
